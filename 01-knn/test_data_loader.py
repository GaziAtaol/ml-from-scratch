from data_loader import load_data, normalize_label, get_num_attributes

train = load_data('training-data/iris_training_1.txt')
test  = load_data('test-data/iris_test_1.txt')

print('Training:', len(train))
print('Test:', len(test))
print('Attribute number:', get_num_attributes(train))
print('first example:', train[0])
print('Original: Iris    SetOsA    ')
print('normalize test:', normalize_label('Iris    SetOsA    '))