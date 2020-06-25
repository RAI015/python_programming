"""
<?xml version'1.0' encording='utf-8' ?>
<root>
    <employee>
        <employ>
            <id>111</id>
            <name>Mike</name>
        </employ>
        <employ>
            <id>222</id>
            <name>Nancy</name>
        </employ>
    </employee>
</root>

{
    "employee":
        [
            {"id": 111, "name": "Mike"},
            {"id": 222, "name": "Nancy"}
        ]
}
"""
import json

j = {
    "employee":
        [
            {"id": 111, "name": "Mike"},
            {"id": 222, "name": "Nancy"}
        ]
}

print(j)
print('##############')
print(json.dumps(j))

a = json.dumps(j)
print('@@@@@@@@@@@@@@')
print(json.loads(a))
print('@@@@@@@@@@@@@@')


with open('test.json', 'w') as f:
    json.dump(j, f)


print('##############')
with open('test.json', 'r') as f:
    print(json.load(f))
