from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import os
from six.moves.urllib.request import urlopen
import numpy as np
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'#Make sure some unneccessary error statements don't pop up
tf.logging.set_verbosity(tf.logging.ERROR)#Remove Tensorflow specific warnings

progTesting = "Testing.csv"
progTestingUrl = ""

def main():
  # If the training and test sets aren't stored locally, download them.

  if not os.path.exists(progTesting):
    raw = urlopen(progTestingUrl).read()
    with open(progTesting, "wb") as f:
      f.write(raw)

  # Load datasets.

  test_set = tf.contrib.learn.datasets.base.load_csv_with_header(
      filename=progTesting,
      target_dtype=np.int,
      features_dtype=np.float32)
  # Define the test inputs
  test_input_fn = tf.estimator.inputs.numpy_input_fn(
      x={"x": np.array(test_set.data)},
      y=np.array(test_set.target),
      num_epochs=1,
      shuffle=False)
 #---------------------------------------------------------------------------------
  #model_dir below has to be the same as the previously specified path!
  feature_columns = [tf.feature_column.numeric_column("x", shape=[30])]
  new_classifier = tf.estimator.DNNClassifier(feature_columns=feature_columns,
                                          hidden_units=[10, 20, 10],
                                          n_classes=2,
                                          model_dir="./model")

  accuracy_score = new_classifier.evaluate(input_fn=test_input_fn)["accuracy"]

  print("\nTest Accuracy: {0:f}\n".format(accuracy_score))

  predict_input_fn = tf.estimator.inputs.numpy_input_fn(
      x={"x": np.array(test_set.data)},
      num_epochs=1,
      shuffle=False)

  predictions = list(new_classifier.predict(input_fn=predict_input_fn))
  predicted_classes = [p["classes"] for p in predictions]

  #Print the predictions (you will get the outputs as integers-which can be mapped to desired output format)
  for i in range(len(predicted_classes)):
      if ((predicted_classes[i][0])  == '1'):
        print('Yes')
      else:
        print('No')
if __name__ == "__main__":
    main()