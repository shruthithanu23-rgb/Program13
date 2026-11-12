import React, { useState } from "react";
function App() {
const [users, setUsers] = useState(10);
return (
<div style={{ fontFamily: "Arial" }}>
<div style={{
backgroundColor: "blue",
color: "white",
padding: "15px"
}}>
<h2>My Dashboard</h2>
</div>
<div style={{
width: "200px",
height: "400px",
backgroundColor: "lightgray",
padding: "20px",
float: "left"
}}>
<h3>Menu</h3>
<p>Home</p>
<p>Users</p>
<p>Reports</p>
</div>
<div style={{ marginLeft: "250px", padding: "20px" }}>
<h2>Dashboard</h2>
<div style={{
display: "flex",
gap: "20px"
}}>
<div style={{
padding: "20px",
backgroundColor: "lightblue"
}}>
<h3>Total Users</h3>
<h2>{users}</h2>
</div>
<div style={{
padding: "20px",
backgroundColor: "lightgreen"
}}>
<h3>Total Orders</h3>
<h2>25</h2>
</div>
<div style={{
padding: "20px",
backgroundColor: "lightpink"
}}>
<h3>Total Sales</h3>
<h2>5000</h2>
</div>
</div>
<br />
<button onClick={() => setUsers(users + 1)}>
Add User
</button>
</div>
</div>
);
}
export default App; 