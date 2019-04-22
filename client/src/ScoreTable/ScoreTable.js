import React, { Component } from 'react';
import { withStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

const styles = theme => ({
  root: {
    width: '100%',
    marginTop: theme.spacing.unit * 3,
    overflowX: 'auto',
  },
  table: {
    minWidth: 700,
  },
});


class ScoreTable extends Component {
  constructor(props) {
    super(props)

    this.state = {data: []}
  }
  componentDidMount() {
    fetch("http://localhost:5000", {method: 'GET', dataType:'json'})
      .then(r => r.json())
      .then(r => {
        for(let i = 0; i < r.length; i++) {
          let row = r[i];
          if (row.day == null) {
            row.day = "-"
          }
          if (row.month == null) {
            row.month = "-"
          }
        }
        this.setState((state) => {
          return {data: r}
        })
      })
      .catch(err => console.log(err))
  }
  render() {
    const { data } = this.state;
    console.log(data)
    return (
      <div>
        <Paper>
          <Table>
              <TableHead>
                <TableRow>
                  <TableCell>Topic</TableCell>
                  <TableCell>Day</TableCell>
                  <TableCell>Month</TableCell>
                  <TableCell>Year</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {data.map(row => {
                  return (
                    <TableRow key={row.id}>
                      <TableCell component="th" scope="row">
                        {row.topic}
                      </TableCell>
                      <TableCell>{row.day}</TableCell>
                      <TableCell>{row.month}</TableCell>
                      <TableCell>{row.year}</TableCell>
                    </TableRow>
                  );
                })}
              </TableBody>
            </Table>
          </Paper>
      </div>
    )
  }
}


export default withStyles(styles)(ScoreTable);
