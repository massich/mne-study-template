[![CircleCI](https://circleci.com/gh/mne-tools/mne-study-template.svg?style=svg)](https://circleci.com/gh/mne-tools/mne-study-template)

Study analysis template with MNE
================================

First you will need to update the [config.py](config.py) file. This
file is meant to contain study specific parameters:

- `plot` : if True, the single scripts generate plots

#### DIRECTORIES
- `study_path` : path to the directory that contains your data.
- `subjects_dir` : path pointing to the antomical files for all subjects
- `meg_dir` : path pointing to the MEG files for all subjects

#### SUBJECTS / RUNS
- `study_name` : the name of your experiment
- `subjects` : a list of the subject names
- `exclude_subjects` : the list of subjects to exclude from the above
- `runs` : list of strings that specifies how your runs are named. For example `runs = ['run01', 'run02']`. If you have only one run it should be `runs = ['']`.
- `base_raw_fname` : string that describes how your files are named. For example: `'{subject}_audvis_{run}_raw.fif'`

#### BAD CHANNELS
- `bads` : to be removed before maxfilter is applied (defined per run)

#### DEFINE ADDITIONAL CHANNELS
- `set_channel_types` : set channel type of extra channels that were recorded (e.g. EOG, ECG etc.) Example: set type for EEG062 as EOG.
- `rename_channels` : rename channels. Example: rename channel EEG062 to EOG062.
- `bads` : dictionary containing he list of bad channels for each subject

#### FREQUENCY FILTERING
- `h_freq` : the high-frequency cut-off in the lowpass filtering step. Keep it None if no lowpass filtering should be applied.
- `l_freq` : the low-frequency cut-off in the highpass filtering step. Keep it None if no highpass filtering should be applied.

#### MAXFILTER PARAMETERS
- `mf_ctc_fname` : for maxfiltering, path to the cross talk file on this machine.
- `mf_cal_fname` : for maxiltering, path to the calibration file on this machine.
- `mf_reference_run` : specify which run to use for HPI recalibration, all other runs will have head position adjusted to this one.
- `mf_head_origin`: The origin of the head used for maxwell filtering. 
- `mf_st_duration`: a float that specifies the buffer duration in seconds. As an example, 10s acts like a 0.1 Hz highpass filter. If None (default), no temporal spatial filtering is applied during MaxFilter.

#### RESAMPLING
- `resample_sfreq` : a float that specifies at which sampling frequency the data should be resampled. If None then no resampling will be done.
- `decim` : integer that says how much to decimate data at the epochs level. It is typically an alternative to the `resample_sfreq` parameter.

#### AUTOMATIC REJECTION OF ARTIFACTS
- `reject` : the default rejection limits to make some epochs as bads. This allows to remove strong transient artifacts. **Note**: these numbers tend to vary between subjects.

#### EPOCHING
- `tmin`: float that gives the start time before event of an epoch.
- `tmax` : float that gives the end time after event of an epochs.
- `baseline` : tuple that specifies how to baseline the epochs. If None, then no baseline applied.
- `event_id` : python dictionary that maps events (trigger/marker values) to conditions. E.g. `event_id = {'Auditory/Left': 1, 'Auditory/Right': 2}`
- `runica` : boolean that says if ICA should be used or not.

#### ICA PARAMETERS
- ``runica`` : boolean that says if ICA should be used or not.

#### DECODING 
- `decoding_conditions`: list of tuples of strings that contain the conditions to compare. For example: `[('Auditory/Left', 'Auditory/Right'), ('Auditory', 'Visual')]`
- `decoding_metric` : the scikit-learn scoring metric to use. For example: 'roc_auc' or 'accuracy'
- `decoding_n_splits` : the number of splits to use in the cross-validation. For example 5 that will mean 5-folds cross-validation.

#### TIME-FREQUENCY
- `time_frequency_conditions`:

#### ADVANCED
- `l_trans_bandwidth` : float that specifies the transition bandwidth of the highpass filter. By default it's `'auto'` and uses default mne parameters.
- `h_trans_bandwidth` : float that specifies the transition bandwidth of the lowpass filter. By default it's `'auto'` and uses default mne parameters.
- `N_JOBS` : an integer that specifies how many subjects you want to run in parallel.


Preprocessing steps
-------------------

| Script      | Description                                                |
|:-----------:|:----------------------------------------------------------:|
| [01-frequency_filtering.py](01-frequency_filtering.py) | Read raw data and apply lowpass or/and highpass filtering |
| [02-maxwell_filtering.py](02-maxwell_filtering_sss.py) | Run maxfilter and do lowpass filter at 40 Hz. |
| [03-extract_events.py](03-extract_events.py) | Extract events or annotations or markers from the data and save it to disk. Uses events from stimulus channel STI101. |
| [04-artifact_correction_ica.py](04-artifact_correction_ica.py) | Run Independant Component Analysis (ICA) for artifact correction. |
| [05-artifact_correction_ssp.py](04-artifact_correction_ssp.py) | Run Signal Subspace Projections (SSP) for artifact correction. These are often also referred to as PCA vectors. |
| [05-make_epochs.py](05-make_epochs.py) | Extract epochs. |
| [06-make_evoked.py](06-make_evoked.py) | Extract evoked data for each condition. |

To Do
-------------------
- add visualization options
- description of how to debug/ run script in interactive mode
- work on artifact rejection scripts (04_)
- document the scripts

Getting started
---------------

First, you need to make sure you have mne-python installed and working on your system. See [installation instructions](http://martinos.org/mne/stable/install_mne_python.html) and once is done you should be able to run in a terminal this:

    $ python -c "import mne; mne.sys_info()"

Once you have mne-python installed on your machine you need the analysis script that you'll need to adjust to your need. You can [download](https://github.com/mne-tools/mne-study-template/archive/master.zip) the current version of these script, or get them through git:

	$ git clone https://github.com/mne-tools/mne-study-template.git

For source analysis you'll also need freesurfer, follow the instructions on [their website](https://surfer.nmr.mgh.harvard.edu/).

Authors
-------

- [Mainak Jas](http://perso.telecom-paristech.fr/~mjas/), Telecom ParisTech, Université Paris-Saclay
- [Eric Larson](http://larsoner.com), University of Washington ILABS
- [Denis Engemann](http://denis-engemann.de), Neurospin, CEA/INSERM, UNICOG Team
- Jaakko Leppäkangas, Telecom ParisTech, Université Paris-Saclay
- [Samu Taulu](http://ilabs.washington.edu/institute-faculty/bio/i-labs-samu-taulu-dsc), University of Washington, ILABS
- [Matti Hämäläinen](https://www.martinos.org/user/5923), Martinos Center, MGH, Harvard Medical School
- [Alexandre Gramfort](http://alexandre.gramfort.net), INRIA, Université Paris-Saclay
