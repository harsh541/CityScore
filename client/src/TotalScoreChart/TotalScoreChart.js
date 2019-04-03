import React, { Component } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ReferenceLine } from 'recharts';


var data = [
  {
    name: 'A', Score: 0
  },
  {
    name: 'B', Score: 0
  },
  {
    name: 'C', Score: 0
  },
  {
    name: 'D', Score: 0
  },
  {
    name: 'E', Score: 0
  },
  {
    name: 'F', Score: 0
  },
  {
    name: 'G', Score: 0
  },
];

for (let i = 0; i < data.length; i++) {
  data[i].Score = Math.round((Math.random() + 1 )* 100) / 100
}

class TotalScoreChart extends Component {
  render() {
    return (
      <div>
        <LineChart
          width={1200}
          height={300}
          data={data}
          margin={{
            top: 5, right: 30, left: 20, bottom: 5,
          }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Legend />
          <ReferenceLine x="C" stroke="green" label="Today" />
          <Line type="monotone" dataKey="Score" stroke="blue" />
        </LineChart>
      </div>
    )
  }
}

export default TotalScoreChart