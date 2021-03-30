import mne
import numpy


def load_epochs(raw):
    evts,evts_dict = mne.events_from_annotations(raw)
    wanted_keys = [e for e in evts_dict.keys() if "stimulus" in e]
    evts_dict_stim=dict((k, evts_dict[k]) for k in wanted_keys if k in evts_dict)
    epochs = mne.Epochs(raw,evts,evts_dict_stim,tmin=-0.5,tmax=1,reject_by_annotation=False)
    
    return epochs, evts_dict
	

def save_array(filename, to_save):
    '''
    saves the array in a file with the given filename
    '''
    with open(filename, 'wb') as f:
        numpy.save(f, to_save)
		

def load_array_from_memory(filename):
    '''
    loads the array from the file with the given filename
    '''
    with open(filename, 'rb') as f:
        arr = numpy.load(f)
    return arr

	
def get_timepoints(epoch_start, epoch_end, number_of_datapoints):
	"""
	calculates equidistant timepoints in the time range
	"""
	time_range = numpy.abs(epoch_end) + numpy.abs(epoch_start)
	steps = time_range / number_of_datapoints
	x = numpy.arange(start=epoch_start, stop=epoch_end, step=steps)
	return x