# deltaQ

We want to build a product.  The product can identify linearly dependent variables in a vector.  The client interface is a website with an input to specify a data file and a button to start the analysis and return the result.  The data analysis needs to run in a different environment from the webserver. We want to deploy it separately from the UI.  It gets triggered by an http post on a specific url.  The data file is stored on Amazon S3. 

To test the product it should be deployable locally on any computer with docker.  The test version should be fully functional, except that the file can be contained in the docker-container of the UI instead of getting it from S3. Therefore I attach the file in this mail. 

We build a technical proof of concept of the product and present it to the technical director of the company (during the interview). 

The expected output is fix it to the indexes (or labels) of linearly dependent columns.
