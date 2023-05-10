import React, { useState } from 'react';
import './App.css';



function App() {

  // new line start
  const [profileData, setProfileData] = useState(null)

  function getData() {

    fetch('/profile')
    .then((response) => {
      const res = response.data
      
      setProfileData(({
        profiles: res.profiles
      }))

     

    }).catch((error) => {
      if (error.response) {
        console.log(error.reponse)
        console.log(error.response.status)
        console.log(error.response.headers)
      }
    })


  }
  
  function profileList() {
    const pList = profileData.profiles.map(( profile, i)  => 
      <p>
      <ul key={i}>
        <li>{profile.name}</li>
        <li>{profile.about}</li>
        <li><img src={profile.image} width="250px" height="250px" alt={profile.name}></img></li>
      </ul>
      </p>
    
      );


      return <ul>{pList}</ul>
  }
  
  console.log(profileData)

  return (
    <div className="App">
      <header className="App-header">
        <p>To get the profile details: </p><button onClick={getData}>Click me</button>
        {profileData && <div>
             {profileList()}
            </div>
        }                            
      </header>
    </div>
  );
}

export default App;
