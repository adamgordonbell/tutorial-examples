# JQ
https://earthly.dev/blog/jq-select/

## Intro
Hey, in this video I'm going to show you how and why to use JQ to work with JSON files. 

Jq is a powerful tool that... but for the longest time I mainly just used it to pretty print json. Occasionally I would do more complex things but always had to google right incantation first....

Let's fix that. I'll show you how to understand JQ and then you'll be able to do whatever you want with JSON, without much thought.

## Object Identifier

echo '{"key1":{"key2":"value1"}}' | jq '.'

curl https://api.github.com/repos/jqlang/jq

curl https://api.github.com/repos/jqlang/jq | jq ' .name'

curl https://api.github.com/repos/jqlang/jq | jq ' .owner'

curl https://api.github.com/repos/jqlang/jq | jq ' .owner.login'

## Lesson: Object Identifier-Index

jq '.key.subkey.subsubkey'

## Arrays

curl https://api.github.com/repos/jqlang/jq/issues?per_page=5

curl https://api.github.com/repos/jqlang/jq/issues?per_page=5 | jq '.[4]'

echo "[1,2,3,4,5]" | jq '.[2:4]'

echo "[1,2,3,4,5]" | jq '.[2:]'

echo "[1,2,3,4,5]" | jq '.[-2:]'

curl https://api.github.com/repos/jqlang/jq/issues?per_page=5 | \
 jq '.[4].title'

curl https://api.github.com/repos/jqlang/jq/issues?per_page=5 | \
 jq '.[].title'

### Side Note: Command Line Stuff

echo '["1","2","3"]' | jq -r '.[]'

## Lesson: Arrays

- You can select array elements, or whole array
jq '.key[].subkey[2]

## Array Constructors

- JQ likes to returns things one at a time
echo '""' | jq '1,2' 

- Wrap it up
echo '""' | jq '[1,2]' 

- Real world use
curl https://api.github.com/repos/jqlang/jq/issues?per_page=5 | \
  jq '[ .[].title ] ' 

## Lesson - Array Constructor

echo '[{"a":"b"},{"a":"c"}]' | jq -r '.[].a'

echo '[{"a":"b"},{"a":"c"}]' | jq -r '[ .[].a ]'

## Object Constructors

curl https://api.github.com/repos/jqlang/jq/issues?per_page=2 | \
 jq '.[] .title, .[] .number'

curl https://api.github.com/repos/jqlang/jq/issues?per_page=2 | \
  jq '[ .[] .title, .[] .number ]'

echo '["Adam","Gordon","Bell"]' | jq -r '.[0], .[2]'

echo '["Adam","Gordon","Bell"]' | \
  jq -r '{ "first_name":.[0], "last_name": .[2]}'

curl https://api.github.com/repos/jqlang/jq/issues?per_page=2 | \
  jq '[ { title: .[].title, number: .[].number } ]'

  curl https://api.github.com/repos/jqlang/jq/issues?per_page=2 | \
  jq '[ .[] | { title, number} ]'

## Lesson: Object Constructors

- Works like this
jq '{ "key1": <<jq filter>>, "key2": <<jq filter>> }'

## Short hand selector

curl https://api.github.com/repos/jqlang/jq/issues/2289 | \
jq '{ title: .title, number: .number }'

curl https://api.github.com/repos/jqlang/jq/issues/2289 | \
jq '{ whats_my_name_Again: .title, thing1: .number }'

curl https://api.github.com/repos/jqlang/jq/issues/2289 | \
jq '{ title, number}'

## Sorting and Counting

curl https://api.github.com/repos/jqlang/jq/issues/2289 | \
jq '{ title, number, labels }'

echo '["3","2","1"]' | jq 'sort'

echo '["3","3","ZZ", "3"]' | jq 'reverse'

echo '["3","2","1"]' | jq 'length'

echo '{"title":"JQ Select"}' | jq '.title' | jq 'length'

echo '{"title":"JQ Select"}' | jq '.title | length'

- All Together

curl https://api.github.com/repos/jqlang/jq/issues/2289 | \
  jq ' { title, number, labels: .labels | sort } '

curl https://api.github.com/repos/jqlang/jq/issues/2560 | \
jq ' { title, number, labels: .labels | sort_by(.name) } '

curl https://api.github.com/repos/jqlang/jq/issues/2560 | \
  jq ' { title, number, labels_count: .labels | length } '  


## Lesson: Pipes and functions (filters)

- You can combine things together with pipes
- There are built in functions and you can write your own
 - They act as filters

## Earthly

 - Ok, the last and coolest things I've got to show is bring this all together.
- But first I want to tell you a little about Earthly.
- Earthly, is a open source build tool.
- No software developer likes their build pipeline.
- Nobody likes waiting for a build to finish, or rerunning things because the build is flaky.
- With Earthly, you write your build in a format similar to a Dockerfile, or a make file and you can run your build locally or in CI.
- You'd be surprized how big of a difference this can make and because the build runs in a container, it runs the same on your local as it does in CI. 
- It's like docker, but for CI. Go to EArthly.dev, or like in the description to check it out.
- Alright, now let me show you how to bring all this JQ skills together.


## Maps and Selects

curl https://api.github.com/repos/jqlang/jq/issues?per_page=100 | \
  jq '[ .[] | { title, number, labels_count: .labels | length, title_length: .title | length } ]'  

curl https://api.github.com/repos/jqlang/jq/issues?per_page=100 | \
  jq 'map({ title, number, labels_count: .labels | length , title_length: .title | length } ) | map(select(.title_length > 30))'  
  

curl https://api.github.com/repos/jqlang/jq/issues?per_page=5000 | \
  jq 'map({ title, number, url: ("https://github.com/jqlang/jq/issues/" +  (.number | tostring)), title_length: .title | length } ) | sort_by(.title_length)| reverse | .[0:2]'  


## Review

jq '.key[0].subkey[2:3].subsubkey'

jq '[ { key1: .key1, key2: .key2 }  ]'

jq 'map({ order-of-magitude: .items | length | tostring | length }) 

## Outro

If you looking to learn more about building software, subscribe to the channel. If you want to learn more about Earthly, check the link in the description. 

And let me know your JQ questions in the comments. It might inspire a new vidoe. 
In fact, let me know whatever you want to see in a video.