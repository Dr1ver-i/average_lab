import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="平均数AI实验室",
    page_icon="📊"
)


st.title("📊 平均数AI实验室")
st.write("自由设置数据数量，输入数据名称和数值，观察平均数变化")


# =====================
# 设置数据数量
# =====================

st.sidebar.header("⚙️ 实验设置")


number = st.sidebar.number_input(
    "请输入数据数量",
    min_value=1,
    max_value=50,
    value=5,
    step=1
)


st.sidebar.write(
    f"当前设置：{number} 个数据"
)



# =====================
# 输入数据
# =====================

st.subheader("📝 输入数据")


names = []
values = []


for i in range(int(number)):

    col1, col2 = st.columns(2)


    with col1:
        name = st.text_input(
            f"第 {i+1} 个数据名称",
            value=f"数据{i+1}",
            key=f"name_{i}"
        )


    with col2:
        value = st.number_input(
            f"{name} 的数值",
            min_value=0.0,
            max_value=10000.0,
            value=50.0,
            key=f"value_{i}"
        )


    names.append(name)
    values.append(value)



# =====================
# 数据处理
# =====================


data = pd.DataFrame(
    {
        "名称": names,
        "数值": values
    }
)


st.subheader("📋 数据展示")

st.dataframe(data)



total = sum(values)

average = total / number



# =====================
# 结果显示
# =====================

col1,col2,col3 = st.columns(3)


with col1:
    st.metric(
        "数据数量",
        number
    )


with col2:
    st.metric(
        "总和",
        round(total,2)
    )


with col3:
    st.metric(
        "平均数",
        round(average,2)
    )



# =====================
# 图表
# =====================

st.subheader("📊 数据变化图")


fig = px.bar(
    data,
    x="名称",
    y="数值",
    text="数值"
)


fig.add_hline(
    y=average,
    annotation_text=f"平均数={average:.2f}"
)


st.plotly_chart(fig)



# =====================
# AI解释
# =====================

st.subheader("🤖 AI数学助手")


max_value=max(values)
min_value=min(values)


if max_value-min_value > average:

    st.warning(
        f"""
        数据差异比较大。

        最高数据：
        {max_value}

        最低数据：
        {min_value}

        如果提高较低的数据，平均数会增加。
        """
    )

else:

    st.success(
        f"""
        数据比较均衡。

        当前平均数：
        {average:.2f}

        大多数数据接近平均水平。
        """
    )



# =====================
# 数学过程
# =====================

st.subheader("✏️ 平均数计算")


st.write(
    f"""
    数据总和：

    {total:.2f}


    数据个数：

    {number}


    平均数：

    {total:.2f} ÷ {number}

    = **{average:.2f}**
    """
)
