# mongodb
<h2>INTRO:</h2>
<p>db.createCollection("employees")</p>



<h2>EXIT:</h2>
<p>
  use admin<br>
  db.shutdownServer()<br>
  exit<br>
</p>


<h2>CMD OPTIONS:</h2>
<p>
  mongod --help<br>
  mongod --dbPath <directory path><br>
    mongod --port <port number><br>
      mongod --auth<br>
      mongod --bind_ip 123.123.123.123<br>
      mongod --bind_ip localhost,123.123.123.123<br>
</p>

<h2>CONGIURATION FILE:</h2>
<p>
  mongod --config mongod.conf<br>
  mongod -f mongod.conf<br>
</p>

storage:<br>
&nbsp;&nbsp;dbPath: "/data/db"<br>
systemLog:<br>
&nbsp;&nbsp;path: "/data/log/mongod.log"<br>
&nbsp;&nbsp;destination: "file"<br>
replication:<br>
&nbsp;&nbsp;replSetName: M103<br>
net:<br>
&nbsp;&nbsp;bindIp : "127.0.0.1,192.168.103.100"<br>
tls:<br>
&nbsp;&nbsp;mode: "requireTLS"<br>
&nbsp;&nbsp;certificateKeyFile: "/etc/tls/tls.pem"<br>
&nbsp;&nbsp;CAFile: "/etc/tls/TLSCA.pem"<br>
security:<br>
&nbsp;&nbsp;keyFile: "/data/keyfile"<br>
processManagement:<br>
&nbsp;&nbsp;fork: true<br>

<h3>Create a super user when auth will be enabled</h3>
mongo admin --host localhost:27000 --eval '<br>
db.createUser({<br>
user: "m103-admin",<br>
pwd: "m103-pass",<br>
roles: [<br>
{role: "root", db: "admin"}<br>
]<br>
})<br>
'<br>
<h3>mongod.conf</h3>
<p>
  net:<br>
  &nbsp;&nbsp;host: 127.0.0.1<br>
  &nbsp;&nbsp;port: 27000<br>
  security:<br>
  &nbsp;&nbsp;authorization: enabled<br>
</p>

<h2>COMMANDS</h2>
<h3>User management commands:</h3>
<p>
  db.createUser()<br>
  db.dropUser()<br>
</p>
<h3>Collection management commands:</h3>
<p>
  db.<collection>.renameCollection()<br>
  db.<collection>.createIndex()<br>
  db.<collection>.drop()<br>
</p>
<h3>Database management commands:</h3>
<p>
  db.dropDatabase()<br>
  db.createCollection()<br>
</p>
<h3>Database status command:</h3>
<p>
  db.serverStatus()<br>
</p>

<h3>Creating index with Database Command:</h3>
<code>
  db.runCommand(<br>
  { "createIndexes": &lt;collection> },<br>
  { "indexes": [
    {
      "key": { "product": 1 }
    },
    { "name": "name_index" }
    ]
  }<br>
)
</code>
<h3>Creating index with Shell Helper:</h3>
<code>
  db.&lt;collection>.createIndex(<br>
  { "product": 1 },<br>
  { "name": "name_index" }<br>
)
</code>
<h3>Introspect a Shell Helper:</h3>
<code>db.&lt;collection>.createIndex</code><br>