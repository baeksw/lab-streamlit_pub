import streamlit as st
import pandas as pd
import numpy as np

# 데이터 로드 및 처리 (가상 데이터 사용)
data = pd.DataFrame({
    '프로젝트': ['프로젝트 A', '프로젝트 B', '프로젝트 C'],
    '상태': ['진행 중', '완료', '보류'],
    '마감 기한': ['2024-03-01', '2024-02-15', '2024-04-20'],
    '담당자': ['김팀장', '이매니저', '박코디']
})

# 상단 패널 - 프로젝트 상태 개요
st.header("프로젝트 상태 개요")
status_summary = data['상태'].value_counts()
for status, count in status_summary.items():
    st.metric(label=status, value=count)

# 중앙 패널 - 업무 분포 및 우선순위
st.header("업무 분포")
st.bar_chart(data['상태'].value_counts())

# 하단 패널 - 마감 기한 및 진행 중인 작업/이슈
st.header("마감 기한")
st.table(data.sort_values('마감 기한'))

# 사이드바 필터링
selected_status = st.sidebar.selectbox('상태 필터링', data['상태'].unique())
filtered_data = data[data['상태'] == selected_status]
st.dataframe(filtered_data)
