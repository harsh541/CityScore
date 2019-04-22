import React, { Component } from 'react';
import Gauge from 'react-svg-gauge';


class TotalScore extends Component {
  constructor(props) {
    super(props);

    this.state = {data: [], score: 0}
  }

  componentDidMount() {
    fetch("http://localhost:5000", {method: 'GET', dataType:'json'})
      .then(r => r.json())
      .then(r => {
        let dayScore = 0;
        for(let i = 0; i < r.length; i++) {
          let row = r[i];
          if (row.day == null) {
            row.day = "-"
            dayScore += 0;
          }
          if (row.month == null) {
            row.month = "-"
          }
          else if (row.day != null) {
            dayScore += row.day;
          }
        }
        dayScore = Math.round((dayScore / r.length) * 100) / 100;
        this.setState((state) => {
          return {data: r, score: dayScore}
        })
      })
      .catch(err => console.log(err))
  }

  render() {
    const { score } = this.state;

    return (
      <div>
        <Gauge value={score} min={0} max= {2} color={"#ADC4DD"}width={400} height={250} label={""} valueLabelStyle={{fontSize: 50}}/> 
      </div>

    )
  }
}


export default TotalScore;