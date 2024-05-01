import React from "react";

export const Features = (props) => {
  return (
    <div id="features" className="text-center">
      <div className="container">
        <div className="a">
          <h2>Features</h2>
        </div>
        <div className="row">
          {props.data
            ? props.data.map((d, i) => (
                <div key={`${d.title}-${i}`} className="col-xs-6 col-md-3">
                  {" "}
                  <img src={d.img} alt={d.title} className="img-fluid" />
                  <h3>{d.title}</h3>
                  <p>{d.text}
                  <br />
                  <a href={d.link} target="blank">Start Chat</a>
                  </p>


                </div>
              ))
            : "Loading..."}
        </div>
      </div>
    </div>
  );
};
