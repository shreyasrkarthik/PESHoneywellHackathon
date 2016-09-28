<?php
  
  $con = new mysqli("localhost","root","crap","Honeywell");
  if ($con->connect_error)
  {
      die('Could not connect to the server');
  }
  $user_name= $_GET['user_name'];
  $sql = "SELECT floor,pillar,post FROM router_floor_table,user_rmac_table where user_rmac_table.u_name='$user_name' && user_rmac_table.u_router_mac=router_floor_table.router_mac";
  $result = mysqli_query($con,$sql);
  if ($result)
  {
      while($row = $result->fetch_assoc()) 
      {
        echo "" . $row["floor"]. " " . $row["pillar"]. " " . $row["post"];
      }
  }      
  else
  {
    die("No users found");  
  }
  mysqli_close($con);
?>
