from nilearn.datasets.utils import _get_dataset_dir, _fetch_files


def download_ibc_3mm(sub, ses, img_id, confound_id, dir):
    data_dir = _get_dataset_dir(f'3mm/{sub}/{ses}', data_dir='data')
    url = f'https://osf.io/{img_id}/download'
    _fetch_files(
        data_dir,
        [(f'wrdc{sub}_{ses}_task-RestingState_dir-{dir}_bold.nii.gz',
          url,
          {'move': f'wrdc{sub}_{ses}_task-RestingState_dir-ap_bold.nii.gz'})]
    )
    url = f'https://osf.io/{confound_id}/download'
    _fetch_files(
        data_dir,
        [(f'dir-{dir}_confounds_timeseries.tsv',
          url,
          {'move': f'dir-{dir}_confounds_timeseries.tsv'})]
    )
