# Node.js API Auth Example

## Example API Requests

```
export BASE_URL=https://us-central1-cloud-function-test-187308.cloudfunctions.net/http
```

## Deployment to Google Cloud Functions

```
serverless deploy
```

## Setting Up Deployment

* Register with Google Cloud Platform, create a project
* Follow the serverless quickstart instructions for hello world (for credentials and enabling APIs)
* Install the [Google Cloud SDK](https://cloud.google.com/sdk/docs)
* Update/install gcloud components: `gcloud components update && gcloud components install beta`
* Initialize gcloud: `gcloud init`

## PostgreSQL

NOTE: It seems Cloud SQL is not supported for Google Functions yet.

You can connect with `gcloud sql` or with `psql`:

```
gcloud sql connect test-instance --user=postgres
psql "sslmode=disable dbname=api-auth user=postgres hostaddr=35.195.106.111"
```

## Google Cloud Spanner

NOTE: Google Cloud Spanner is a large scale database and costs at least around a dollar an hour.

* Get index.js and package.json from [official example code](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/tree/master/functions/spanner)
* Create cloud storage bucket: `gsutil mb -p cloud-function-test-187308 gs://api-auth`
* Test deploy: `gcloud beta functions deploy get --stage-bucket api-auth --trigger-http`

## Resources

* [Serverless Google Quickstart](https://serverless.com/framework/docs/providers/google/guide/quick-start/)
* [Using Cloud Spanner with Cloud Functions](https://cloud.google.com/spanner/docs/use-cloud-functions)
* [Quickstart for Cloud SQL for PostgreSQL](https://cloud.google.com/sql/docs/postgres/quickstart)
* [Could Functions - Supported Services](https://cloud.google.com/functions/docs/concepts/services)
