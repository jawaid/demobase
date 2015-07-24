# demobase

* Used to create base image for use in the Shippable demos
* For demo purposes, after generating image, flatten the image by:
  * Run demobase in a container
  * Export the container and import it to a new image
  * Push the flattened image to shippabledemo/demobase
