# JQ
https://earthly.dev/blog/jq-select/

# Intro
Hey, in this video I'm going to show you how and why to use JQ to work with JSON files. 

Jq is a powerful tool that... but for the longest time I mainly just used it to pretty print json. Occasionally I would do more complex things but always had to google right incantation first....

Let's fix that. I'll show you how to understand JQ and then you'll be able to do whatever you want with JSON, without much thought.

# Object Identifier

echo '{"key1":{"key2":"value1"}}' | jq '.'

curl https://api.github.com/repos/stedolan/jq

curl https://api.github.com/repos/stedolan/jq | jq ' .name'

curl https://api.github.com/repos/stedolan/jq | jq ' .owner'

curl https://api.github.com/repos/stedolan/jq | jq ' .owner.login'

## Lesson: Object Identifier-Index

jq '.key.subkey.subsubkey'

# Arrays

curl https://api.github.com/repos/stedolan/jq/issues?per_page=5

curl https://api.github.com/repos/stedolan/jq/issues?per_page=5 | jq '.[4]'

echo "[1,2,3,4,5]" | jq '.[2:4]'

echo "[1,2,3,4,5]" | jq '.[2:]'

echo "[1,2,3,4,5]" | jq '.[-2:]'

curl https://api.github.com/repos/stedolan/jq/issues?per_page=5 | \
 jq '.[4].title'


curl https://api.github.com/repos/stedolan/jq/issues?per_page=5 | \
 jq '.[].title'

### Side Note: Command Line Stuff
echo '["1","2","3"]' | jq -r '.[]'

## Lesson: Arrays
- You can select array elements, or whole array
jq '.key[].subkey[2]

# Array Constructors

- JQ likes to returns things one at a time
echo '""' | jq '1,2' 

- Wrap it up
echo '""' | jq '[1,2]' 

- Real world use
curl https://api.github.com/repos/stedolan/jq/issues?per_page=5 | \
  jq '[ .[].title ] ' 

## Lesson - Array Constructor

echo '[{"a":"b"},{"a":"c"}]' | jq -r '.[].a'

echo '[{"a":"b"},{"a":"c"}]' | jq -r '[ .[].a ]'

# Object Constructors

curl https://api.github.com/repos/stedolan/jq/issues?per_page=2 | \
 jq '.[] |  .title, .number'

curl https://api.github.com/repos/stedolan/jq/issues?per_page=2 | \
  jq '[ .[] |  .title, .number ]'

echo '["Adam","Gordon","Bell"]' | jq -r '.[0], .[2]'

echo '["Adam","Gordon","Bell"]' | \
  jq -r '{ "first_name":.[0], "last_name": .[2]}'

curl https://api.github.com/repos/stedolan/jq/issues?per_page=2 | \
  jq '[ .[] | { title: .title, number: .number} ]'

  curl https://api.github.com/repos/stedolan/jq/issues?per_page=2 | \
  jq '[ .[] | { title, number} ]'

## Lesson: Object Constructors

- Works like this
jq '{ "key1": <<jq filter>>, "key2": <<jq filter>> }'

# Sorting and Counting

curl https://api.github.com/repos/stedolan/jq/issues/2289 | \
jq '{ title, number, labels }'

echo '["3","2","1"]' | jq 'sort'

echo '["3","2","1"]' | jq 'reverse'

echo '["3","2","1"]' | jq 'length'

echo '{"title":"JQ Select"}' | jq '.title' | jq 'length'

echo '{"title":"JQ Select"}' | jq '.title | length'

- All Together

curl https://api.github.com/repos/stedolan/jq/issues/2289 | \
  jq ' { title, number, labels: .labels | sort } '

curl https://api.github.com/repos/stedolan/jq/issues/2289 | \
  jq ' { title, number, labels_count: .labels | length } '  

## Lesson: Pipes and functions (filters)
- You can combine things together with pipes
- There are built in functions and you can write your own
-- They act as filters

# Maps and Selects

curl https://api.github.com/repos/stedolan/jq/issues?per_page=100 | \
  jq '[ .[] | { title, number, labels_count: .labels | length, title_length: .title | length } ]'  

curl https://api.github.com/repos/stedolan/jq/issues?per_page=100 | \
  jq 'map({ title, number, labels_count: .labels | length , title_length: .title | length } ) | map(select(.title_length > 30))'  

## Review

jq '.key[0].subkey[2:3].subsubkey'

jq '[ { key1: .key1, key2: .key2 }  ]'

jq 'map({ order-of-magitude: .items | length | tostring | length }) 


