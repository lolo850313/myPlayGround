<template>
  <div>
    <select
      class="form-control"
      :placeholder="placeholder"
      :disabled="disabled"
    ></select>
  </div>
</template>

<script>
  export default {
    name: "Select2",
    data() {
      return {
        select2: null
      };
    },
    model: {
      event: "change", // 使用change作为自定义事件
      prop: "value" // 使用value字段，故这里其实不用写也可以
    },
    props: {
      placeholder: {
        type: String,
        default: ""
      },
      options: {
        type: Array,
        default: []
      },
      disabled: {
        type: Boolean,
        default: false
      },
      value: null
    },
    watch: {
      options(val) {
        // 若选项改变，则更新组件选项
        this.setOption(val);
      },
      value(val) {
        // 若绑定值改变，则更新绑定值
        this.setValue(val);
      }
    },
    methods: {
      setOption(val = []) {
        // 更新选项
        this.select2.select2({ data: val });
        // 若默认值为空，且选项非空，则设置为第一个选项的值
        if (!this.value && val.length) {
          const { id, text } = val[0];
          this.$emit("change", id);
          this.$emit("select", { id, text });
          this.select2.select2("val", [id]);
        }
        // 触发组件更新状态
        this.select2.trigger("change");
      },
      setValue(val) {
        this.select2.select2("val", [val]);
        this.select2.trigger("change");
      }
    },
    mounted() {
      // 初始化组件
      this.select2 = $(this.$el)
        .find("select")
        .select2({
          data: this.options
        })
        .on("select2:select", ev => {
          const { id, text } = ev["params"]["data"];
          this.$emit("change", id);
          this.$emit("select", { id, text });
        });
      // 初始化值
      if (this.value) {
        this.setValue(this.value);
      }
    },
    beforeDestroy() {
      // 销毁组件
      this.select2.select2("destroy");
    }
  };
</script>