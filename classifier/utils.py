def train_model(classifier, feature_extractor, scaler, inputs, labels):
    features = feature_extractor(inputs)
    features = features.reshape((features.shape[0], features.shape[-1])).detach().numpy()
    features = scaler.fit_transform(features)

    classifier.fit(features, labels)

def test_model(classifier, feature_extractor, scaler, inputs, labels):
    features = feature_extractor(inputs)
    features = features.reshape((features.shape[0], features.shape[-1])).detach().numpy()
    features = scaler.transform(features)

    return classifier.score(features, labels)