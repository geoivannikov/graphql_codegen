# GraphQL code generator

## Usage

To run script with default arguments:
```bash
python main.py
```

Help with usage arguments for script:
```bash
python main.py -h
```

Example of using a script with custom arguments:
```bash
python main.py -p kotlin -d ./dest/kotlin_dest_folder -src ./graphQLExample.graphql
```

In this case, the script generates `kotlin` files according to GraphQL samples from `graphQLExample.graphql` file and put them in `./dest/kotlin_dest_folder` folder

## Testing

To test code:
```bash
cd tests/
py.test
```

## Coverage_report

To see coverage report:
```bash
open coverage_html/index.html
```
