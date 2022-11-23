from pathlib import Path
import time
import parselmouth as pm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import os

audio_Column = ['Video Name', 'Length', 'Average Band Energy', 'Avg Intensity', 'Max Intensity', 'Mean Intensity', 'Range Intensity', 'SD Intensity', 
		   'Avg Pitch', 'Max Pitch', 'Mean Pitch', 'Range Pitch', 'SD Pitch',
		   'Mean F1', 'Mean F2', 'Mean F3', 'Mean B1', 'Mean B2', 'Mean B3', 'SD F1', 'SD F2', 'SD F3', 
		   'Mean F2/F1', 'Mean F3/F1', 'SD F2/F1', 'SD F3/F1']
audio_row = []

def amplitude(sound):
	x_sample = sound.xs()
	amplitude = sound.values[:,0]

def intensity(sound):
	intensity = sound.to_intensity()
	
	x_sample = intensity.xs()
	y_intensity = intensity.values

	avg_intensity = intensity.get_average(intensity.end_time,intensity.start_time,'ENERGY')
	max_intensity = np.max(y_intensity)
	min_intensity = np.min(y_intensity)
	range_intensity = max_intensity - min_intensity
	sd_intensity = np.std(y_intensity)
	audio_row.extend([avg_intensity, max_intensity, min_intensity, range_intensity, sd_intensity])

def pitch(sound):
	pitch = sound.to_pitch()
	
	x_sample = pitch.xs()
	y_pitch = pitch.to_matrix().values
	
	y_pitch[y_pitch == 0] = np.nan

	avg_pitch =	np.nanmean(y_pitch)
	max_pitch =	np.nanmax(y_pitch)
	min_pitch =	np.nanmin(y_pitch)
	range_pitch	= max_pitch - min_pitch
	sd_pitch = np.nanstd(y_pitch)
	audio_row.extend([avg_pitch, max_pitch, min_pitch, range_pitch, sd_pitch])


def formant(sound):
	formant = sound.to_formant_burg(max_number_of_formants = 5)
	f1 = []
	b1 = []
	f2 = []
	b2 = []
	f3 = []
	b3 = []

	x_sample = formant.xs()

	for x in x_sample:
		f1.append(formant.get_value_at_time(1,x))
		f2.append(formant.get_value_at_time(2,x))
		f3.append(formant.get_value_at_time(3,x))
		b1.append(formant.get_bandwidth_at_time(1,x))
		b2.append(formant.get_bandwidth_at_time(2,x))
		b3.append(formant.get_bandwidth_at_time(3,x))

	mean_f1 = np.mean(f1)
	mean_f2 = np.mean(f2)
	mean_f3 = np.mean(f3)

	mean_b1 = np.mean(b1)
	mean_b2 = np.mean(b2)
	mean_b3 = np.mean(b3)

	sd_f1 = np.std(f1)
	sd_f2 = np.std(f2)
	sd_f3 = np.std(f3)

	mean_f2_by_f1 = np.mean(np.array(f2)/np.array(f1))
	mean_f3_by_f1 = np.mean(np.array(f3)/np.array(f1))
	
	sd_f2_by_f1 = np.std(np.array(f2)/np.array(f1))
	sd_f3_by_f1 = np.std(np.array(f3)/np.array(f1))

	audio_row.extend([mean_f1, mean_f2, mean_f3, mean_b1, mean_b2, mean_b3, sd_f1, sd_f2, sd_f3, 
				mean_f2_by_f1, mean_f3_by_f1, sd_f2_by_f1, sd_f3_by_f1])


def spectrum(sound):
	spectrum = sound.to_spectrum()
	band_energy_spectrum = spectrum.get_band_energy()
	audio_row.append(band_energy_spectrum)

def drawSpectrogram(sound, dynamic_range=70):

	spectrogram = sound.to_spectrogram(window_length=0.05)
	X, Y = spectrogram.x_grid(), spectrogram.y_grid()
	sg_db = 10 * np.log10(spectrogram.values.T)
	plt.pcolormesh(X, Y, sg_db, vmin=sg_db.max() - dynamic_range, cmap='afmhot')
	plt.ylim([spectrogram.ymin, spectrogram.ymax])
	plt.xlabel("time [s]")
	plt.ylabel("frequency [Hz]")
	
	plt.xlim([sound.xmin, sound.xmax])


def start_audio(fileLogic):
    
    
    if not fileLogic.exists():
        print("starting Audio analysis")
        global audio_row
        data = []
        directory = os.fsencode(os.getcwd())
        print(directory)
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            
            if filename.endswith(".wav") or filename.endswith(".mp3"): 
                sound = pm.Sound(filename)
                print(filename)
                audio_row.append(filename)
                end_time = sound.get_total_duration()
                audio_row.append(end_time)
                amplitude(sound)
                spectrum(sound)
                intensity(sound)
                pitch(sound)
                formant(sound)
                data.append(audio_row)
                audio_row = []
            else:
                continue

        df = pd.DataFrame(data = data, columns = audio_Column)
        df.to_csv('./data_save/audioCues.csv')
        
    else:
        print("Some Process in running file")
