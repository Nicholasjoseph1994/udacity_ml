#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    assert len(predictions) == len(ages)
    assert len(net_worths) == len(ages)
    
    data = [(ages[i], net_worths[i], predictions[i] - net_worths[i]) for i in range(len(ages))]

    data = sorted(data, key = lambda x: -x[2])
    cleaned_data = data[len(data)/10:]

    ### your code goes here

    return cleaned_data

