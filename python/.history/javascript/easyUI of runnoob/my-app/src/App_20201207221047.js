import React from 'react';
import { DataGrid, GridColumn, ComboBox, Label } from 'rc-easyui';
 
class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      total: 0,
      pageSize: 20,
      data: this.getData(10000),
      pagePosition: "bottom",
      options: [
        { value: "bottom", text: "Bottom" },
        { value: "top", text: "Top" },
        { value: "both", text: "Both" }
      ]
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
        <h2>Pagination</h2>
        <div style={{ marginBottom: 10 }}>
          <Label htmlFor="c1">Pager on: </Label>
          <ComboBox inputId="c1" style={{ width: 120 }}
            data={this.state.options}
            editable={true}
            panelStyle={{ height: 'auto' }}
            value={this.state.pagePosition}
            onChange={(value) => this.setState({ pagePosition: value })}
          />
        </div>
        <DataGrid 
          style={{ height: 250 }}
          pagination
          {...this.state}
        >
          <GridColumn field="inv" title="Inv No"></GridColumn>
          <GridColumn field="name" title="Name"></GridColumn>
          <GridColumn field="amount" title="Amount" align="right"></GridColumn>
          <GridColumn field="price" title="Price" align="right"></GridColumn>
          <GridColumn field="cost" title="Cost" align="right"></GridColumn>
          <GridColumn field="note" title="Note"></GridColumn>
        </DataGrid>
      </div>
    );
  }
}
 
export default App;