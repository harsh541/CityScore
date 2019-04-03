import React, { Component } from 'react';
import PropTypes from 'prop-types';
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

let id = 0;
function createData(topic, day, week, month, quarter) {
  id += 1;
  return { id, topic, day, week, month, quarter};
}

const topicNames = ['311 Response', 'Grafitti', 'Missed Trash On-Time %', 'Pothole On-Time %', 'Signal Repair On-Time %', 'Sign Installation On-Time %', 'Tree Maintenance On-Time%', 'On-Time Permit Reviews']
function getRows() {
  const rows = [];
  for (let i = 0; i < topicNames.length; i++) {
    rows.push(createData(topicNames[i], Math.round(Math.random() * 100) / 100, Math.round(Math.random() * 100) / 100, Math.round(Math.random() * 100) / 100, Math.round(Math.random() * 100) / 100, Math.round(Math.random() * 100) / 100, Math.round(Math.random() * 100) / 100, Math.round(Math.random() * 100) / 100, Math.round(Math.random() * 100) / 100))
  }
  return rows;
}

const rows = getRows();


class ScoreTable extends Component {
  render() {
    return (
      <div>
        <Paper>
          <Table>
              <TableHead>
                <TableRow>
                  <TableCell>Topic</TableCell>
                  <TableCell numeric>Day</TableCell>
                  <TableCell numeric>Week</TableCell>
                  <TableCell numeric>Month</TableCell>
                  <TableCell numeric>Quarter</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {rows.map(row => {
                  return (
                    <TableRow key={row.id}>
                      <TableCell component="th" scope="row">
                        {row.topic}
                      </TableCell>
                      <TableCell numeric>{row.day}</TableCell>
                      <TableCell numeric>{row.week}</TableCell>
                      <TableCell numeric>{row.month}</TableCell>
                      <TableCell numeric>{row.quarter}</TableCell>
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
