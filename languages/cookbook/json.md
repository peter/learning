# JSON

## Pretty Printing JSON

Python:

```python
import json
def pretty_json(value):
  return json.dumps(value, indent=4, sort_keys=True)
```

## Transforming JSON on the Command Line

JavaScript:

```bash
# Deleting AWS images example:
aws ecr describe-images --repository-name cms > /tmp/images.json
cat /tmp/images.json |grep imageDigest|wc -l
node -e "console.log(JSON.stringify(require('/tmp/images.json').imageDetails.slice(0, 100).map(i => ({imageDigest: i.imageDigest}))))" > /tmp/images-oldest-ids.txt

cat /tmp/images-oldest-ids.txt | tr ',' $'\n'
aws ecr batch-delete-image --repository-name cms --image-ids $(cat /tmp/images-oldest-ids.txt)
```
