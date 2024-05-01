if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

from re import sub

def snake_case(s):
    # Replace hyphens with spaces, then apply regular expression substitutions for title case conversion
    # and add an underscore between words, finally convert the result to lowercase
    return '_'.join(
        sub('([A-Z][a-z]+)', r' \1',
        sub('([A-Z]+)', r' \1',
        s.replace('-', ' '))).split()).lower()

@transformer
def transform(data, *args, **kwargs):
    # Specify your transformation logic here
    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    new_cols = []
    for v in data.columns:
        new_cols.append(snake_case(v))
    data.columns = new_cols
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    assert output['vendor_id'] is not None, 'There is no vendor_id column'
    assert output[output['passenger_count'] <= 0 ]['passenger_count'].count() == 0, 'Some trip have passenger_count <= 0'
    assert output[output['trip_distance'] <= 0 ]['trip_distance'].count() == 0, 'Some trip have trip_distance <= 0'
