import React from 'react';
import { DataGrid, GridColumn } from 'rc-easyui';
 
class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      total: 1000,
      pageSize: 10,
      data: [],
      loading: false
    }
  }
  componentDidMount() {
    this.loadData(this.state.total);
  }
  loadData(total) {
    this.setState({ loading: true })
    setTimeout(() => {
      this.setState({
        data: this.getData(total),
        loading: false
      })
    }, 300)
  }
  getData(total) {
    let data = [];
    for (let i = 1; i <= total; i++) {
      let amount = Math.floor(Math.random() * 1000);
      let price = Math.floor(Math.random() * 1000);
      data.push({
        inv: 'Inv No ' + i,
        name: 'Name ' + i,
        amount: amount,
        price: price,
        cost: amount * price,
        note: 'Note ' + i
      });
    }
    return data;
  }
  render() {
    return (
      <div>
        <h2>Virtual Scroll</h2>
        <DataGrid {...this.state} virtualScroll style={{ height: 250 }}>
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