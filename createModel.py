from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import os
from six.moves.urllib.request import urlopen
import numpy as np
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'#Make sure some unneccessary error statements don't pop up
tf.logging.set_verbosity(tf.logging.ERROR)#Remove Tensorflow specific warnings
# Data sets

progTraining  = "Training.csv"
progTrainingUrl = ""


def main():
  # If the training and test sets aren't stored locally, download them.
  if not os.path.exists(progTraining):
    raw = urlopen(progTrainingUrl).read()
    with open(progTraining, "wb") as f:
      f.write(raw)


  # Load datasets.
  training_set = tf.contrib.learn.datasets.base.load_csv_with_header(
      filename=progTraining,
      target_dtype=np.int,
      features_dtype=np.float32)


  # Specify that all features have real-value data
  feature_columns = [tf.feature_column.numeric_column("x", shape=[30])]

  # Build 3 layer DNN with 10, 20, 10 units respectively.
  classifier = tf.estimator.DNNClassifier(feature_columns=feature_columns,
                                          hidden_units=[10, 20, 10],
                                          n_classes=2,
                                          model_dir="./model/")
  # Define the training inputs
  train_input_fn = tf.estimator.inputs.numpy_input_fn(
      x={"x": np.array(training_set.data)},
      y=np.array(training_set.target),
      num_epochs=None,
      shuffle=True)

  # Train model.
  classifier.train(input_fn=train_input_fn, steps=2000)


if __name__ == "__main__":
    main()