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

<h2>Logging Basics</h2>
<h3>Get the logging components:</h3>
<code>mongo admin --host 192.168.103.100:27000 -u m103-admin -p m103-pass --eval 'db.getLogComponents()'</code>
<h3>Change the logging level:</h3>
<code>mongo admin --host 192.168.103.100:27000 -u m103-admin -p m103-pass --eval 'db.setLogLevel(0, "index")'</code>
<h3>View the logs through the Mongo shell:</h3>
<code>db.adminCommand({ "getLog": "global" })</code>
<h3>View the logs through the command line:</h3>
<h4>Unix:</h4>
<code>tail -f /data/db/mongod.log</code>
<h4>Windows:</h4>
<code>Get-Content -Path .\mongod.log -Tail 5</code>
<h3>Update a document:</h3>
<code>mongo admin --host 192.168.103.100:27000 -u m103-admin -p m103-pass --eval 'db.products.update( { "sku" : 6902667 }, { $set : { "salePrice" : 39.99} } )'</code>
<h3>Look for instructions in the log file with grep:</h3>
<code>grep -i 'update' /data/db/mongod.log</code>

<h2>Profiling the database</h2>
<h3>List collections</h3>
<code>db.runCommand({listCollections: 1})</code>
<h3>Get profiling level:</h3>
<code>mongo newDB --host 192.168.103.100:27000 -u m103-admin -p m103-pass --authenticationDatabase admin --eval 'db.getProfilingLevel()'</code>
<h3>Set profiling level:</h3>
<code>mongo newDB --host 192.168.103.100:27000 -u m103-admin -p m103-pass --authenticationDatabase admin --eval 'db.setProfilingLevel(1)'</code>
<h3>Show collections:</h3>
<code>mongo newDB --host 192.168.103.100:27000 -u m103-admin -p m103-pass --authenticationDatabase admin --eval 'db.getCollectionNames()'</code>
<h3>Set slowms to 0:</h3>
<code>mongo newDB --host 192.168.103.100:27000 -u m103-admin -p m103-pass --authenticationDatabase admin --eval 'db.setProfilingLevel( 1, { slowms: 0 } )'</code>
<h3>Insert one document into a new collection:</h3>
<code>mongo newDB --host 192.168.103.100:27000 -u m103-admin -p m103-pass --authenticationDatabase admin --eval 'db.new_collection.insert( { "a": 1 } )'</code>
<h3>Get profiling data from system.profile:</h3>
<code>mongo newDB --host 192.168.103.100:27000 -u m103-admin -p m103-pass --authenticationDatabase admin --eval 'db.system.profile.find().pretty()'</code>

<h2>Creating a new user</h2>
<p>
  <code>use admin
    db.createUser({
      user: "root",
      pwd: "root123",
      roles : [ "root" ]
    })</code>
    <h3>Login</h3>
    <code>mongo --username root --password root123 --authenticationDatabase admin</code>
    <p>db.stats()</p>
    <p>use admin<br>
      db.shutdownServer()</p>
</p>

<h2>Creating users(Best practices)</h2>
<p>
  <h3>Create security officer:  </h3>
  <code>db.createUser(
    { user: "security_officer",
      pwd: "h3ll0th3r3",
      roles: [ { db: "admin", role: "userAdmin" } ]
    }
  )</code>
  <h3>Create database administrator:  </h3>
  <code>db.createUser(
    { user: "dba",
      pwd: "c1lynd3rs",
      roles: [ { db: "admin", role: "dbAdmin" } ]
    }
  )</code>
  <h3>Grant role to user:  </h3>
  <code>db.grantRolesToUser( "dba",  [ { db: "playground", role: "dbOwner"  } ] )</code>
  <h3>Show role privileges:  </h3>
  <code>db.runCommand( { rolesInfo: { role: "dbOwner", db: "playground" }, showPrivileges: true} )</code>
</p>