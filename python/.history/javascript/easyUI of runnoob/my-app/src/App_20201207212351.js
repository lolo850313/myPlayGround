import React from 'react';
import { DataGrid, GridColumn } from 'rc-easyui';
 
class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      total: 1000,
      data: this.getData(1000),
      pageSize: 20
    }
  }
  getData(total) {
    let data = [];
    for (let i = 1; i <= total; i++) {
      let amount = Math.floor(Math.random() * 1000);
      let price = Math.floor(Math.random() * 1000);
      data.push({
        inv: "Inv No " + i,
        name: "Name " + i,
        amount: amount,
        price: price,
        cost: amount * price,
        note: "Note " + i
      });
    }
    return data;
  }
  render() {
    return (
      <div>
        <h2>DataGrid Sorting</h2>
        <DataGrid
          style={{ height: 250 }}
          data={this.state.data}
          virtualScroll
          total={this.state.total}
          pageSize={this.state.pageSize}
        >
          <GridColumn field="inv" title="Inv No" sortable></GridColumn>
          <GridColumn field="name" title="Name" sortable></GridColumn>
          <GridColumn field="amount" title="Amount" align="right" sortable></GridColumn>
          <GridColumn field="price" title="Price" align="right" sortable></GridColumn>
          <GridColumn field="cost" title="Cost" align="right" sortable></GridColumn>
          <GridColumn field="note" title="Note"></GridColumn>
        </DataGrid>
      </div>
    );
  }
}
 
export default App;