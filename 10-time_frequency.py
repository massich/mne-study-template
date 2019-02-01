"""
================================
09. Time-frequency decomposition
================================

The epoched data is transformed to time-frequency domain using morlet wavelets.
Faces and scrambled data sets are used and for both of them, the average power
and inter-trial coherence are computed and saved to disk. Only channel 'EEG070'
is used to save time.
"""

import os.path as op
import numpy as np

import mne
from mne.parallel import parallel_func

import config

freqs = np.arange(10, 40)
n_cycles = freqs / 3.


def run_time_frequency(subject):
    print("processing subject: %s" % subject)
    meg_subject_dir = op.join(config.meg_dir, subject)
    fname_epochs = op.join(meg_subject_dir, '%s-epo.fif' % subject)

    epochs = mne.read_epochs(fname_epochs)

    for condition in config.time_frequency_conditions:
        this_epochs = epochs[condition]
        power, itc = mne.time_frequency.tfr_morlet(
            this_epochs, freqs=freqs, return_itc=True, n_cycles=n_cycles)

        power.save(
            op.join(meg_subject_dir, '%s_power_%s-tfr.h5'
                    % (subject, condition.replace(op.sep, ''))), overwrite=True)
        itc.save(
            op.join(meg_subject_dir, '%s_itc_%s-tfr.h5'
                    % (subject, condition.replace(op.sep, ''))), overwrite=True)


parallel, run_func, _ = parallel_func(run_time_frequency, n_jobs=config.N_JOBS)
parallel(run_func(subject) for subject in config.subjects_list)
