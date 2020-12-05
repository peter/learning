# AWS CLI

## Tutorial

```sh
# List buckets
aws s3 ls
# Create bucket
export BUCKET_NAME=awesome-backup-files
aws s3 mb s3://$BUCKET_NAME
aws s3 ls

# Uplaod file to bucket
echo 'foobar' > ~/tmp/foobar
aws s3 cp ~/tmp/foobar s3://$BUCKET_NAME
aws s3 ls s3://$BUCKET_NAME

# Download file (to stdout or path)
aws s3 cp s3://$BUCKET_NAME/foobar -
```

## Resources

* [Installation and Configuration](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)
* [s3 sync command](https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html)
