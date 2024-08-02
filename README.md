<div align="center">
  <img src="./image/Logo_RGB.png" width="300">
</div>

# BatteryML: An Open-Source Tool for Machine Learning on Battery Degradation
## Recent News
Official code and data repository of BatteryML: An Open-Source Tool for Machine Learning on Battery Degradation (ICLR 2024). Please star, watch, and fork BatteryML for the active updates! We appreciate any questions and suggestions!

Our paper is now available on [Arxiv](https://arxiv.org/abs/2310.14714) and [ICLR 2024](https://iclr.cc/virtual/2024/poster/17628)!  This paper provides detailed introduction to our design, which we will be actively updating during the development of BatteryML.

## Introduction

The performance degradation of lithium batteries is a complex electrochemical process, involving factors such as the growth of solid electrolyte interface, lithium precipitation, loss of active materials, etc. Furthermore, this inevitable performance degradation can have a significant impact on critical commercial scenarios, such as causing 'range anxiety' for electric vehicle users and affecting the power stability of energy storage systems. Therefore, effectively analyzing and predicting the performance degradation of lithium batteries to provide guidance for early prevention and intervention has become a crucial research topic.

리튬 배터리의 성능 저하는 고체 전해질 계면의 성장, 리튬 침전, 활성 물질의 손실 등과 같은 요인을 포함하는 복잡한 전기화학적 과정입니다. <br>
또한 이러한 불가피한 성능 저하는 전기 자동차 사용자에게 '주행 거리 불안'을 유발하고 에너지 저장 시스템의 전력 안정성에 영향을 미치는 등 중요한 상업적 시나리오에 중대한 영향을 미칠 수 있습니다. <br>
따라서 리튬 배터리의 성능 저하를 효과적으로 분석하고 예측하여 조기 예방 및 개입을 위한 지침을 제공하는 것이 중요한 연구 주제가 되고 있습니다.

To this end, we open source the BatteryML tool to facilitate the research and development of machine learning on battery degradation.
We hope BatteryML can empower both battery researchers and data scientists to gain deeper insights from battery degradation data and build more powerful models for accurate predictions and early interventions.

이를 위해 배터리 성능 저하에 대한 머신 러닝 연구와 개발을 촉진하기 위해 BatteryML 도구를 오픈소스화했습니다. <br> 배터리 연구자와 데이터 과학자 모두가 배터리 성능 저하 데이터에서 더 깊은 인사이트를 얻고 정확한 예측과 조기 개입을 위한 더욱 강력한 모델을 구축할 수 있도록 BatteryML이 도움이 되기를 바랍니다.

## Framework

<!-- <img src="./image/framework.png" width="800"> -->
<img src="./image/framework_new.png" width="800">

## Highlights:
- **Open-source and Community-driven:** BatteryML is an open-source project for battery degradation modeling, encouraging contributions and collaboration from the communities of both computer science and battery research to push the frontiers of this crucial field.
- **A Comprehensive Dataset Collection:** BatteryML includes a comprehensive dataset collection, allowing easy accesses to most publicly available battery data.
- **Preprocessing and Feature Engineering:** Our tool offers built-in data preprocessing and feature engineering capabilities, making it easier for researchers and developers to prepare ready-to-use battery datasets for machine learning.
- **A Wide Range of Models:** BatteryML already includes most classic models in the literature, enabling developers to quickly compare and benchmark different approaches.
- **Extensible and Customizable:** BatteryML provides flexible interfaces to support further extensions and customizations, making it a versatile tool for potential applications in battery research.

---

- 오픈 소스 및 커뮤니티 중심: BatteryML은 배터리 성능 저하 모델링을 위한 오픈 소스 프로젝트로, 컴퓨터 과학 및 배터리 연구 커뮤니티의 기여와 협업을 장려하여 이 중요한 분야의 지평을 넓혀가고 있습니다.
- 포괄적인 데이터 세트 컬렉션: BatteryML에는 포괄적인 데이터 세트 컬렉션이 포함되어 있어 대부분의 공개적으로 사용 가능한 배터리 데이터에 쉽게 액세스할 수 있습니다.
- 전처리 및 기능 엔지니어링: 연구자와 개발자가 머신 러닝에 바로 사용할 수 있는 배터리 데이터 세트를 쉽게 준비할 수 있도록 데이터 전처리 및 특징 엔지니어링 기능이 내장되어 있습니다.
- 광범위한 모델: BatteryML에는 이미 대부분의 고전적인 모델이 포함되어 있어 개발자가 다양한 접근 방식을 빠르게 비교하고 벤치마킹할 수 있습니다.
- 확장 및 커스터마이징 가능: BatteryML은 추가 확장 및 사용자 지정을 지원하는 유연한 인터페이스를 제공하여 배터리 연구의 잠재적 응용 분야를 위한 다용도 도구로 활용할 수 있습니다.



## Dataset
| Data Source | Electrode Chemistry | Nominal Capacity | Voltage Range (V) | RUL dist. | SOC dist. (%) | SOH dist. (%) | Cell Count |
|---|---|---|---|---|---|---|---|
| CALCE | LCO/graphite | 1.1 | 2.7-4.2 | 566±106 | 77±17 | 48±30 | 13 |
| MATR | LFP/graphite | 1.1 | 2.0-3.6 | 823±368 | 93±7 | 36±36 | 180 |
| HUST | LFP/graphite | 1.1 | 2.0-3.6 | 1899±389 | 100±10 | 43±28 | 77 |
| HNEI | NMC_LCO/graphite | 2.8 | 3.0-4.3 | 248±15 | 64±17 | 49±28 | 14 |
| RWTH | NMC/carbon | 1.11 | 3.5-3.9 | 658±64 | 60±24 | 46±22 | 48 |
| SNL | NCA,NMC,LFP/graphite | 1.1 | 2.0-3.6 | 1256±1321 | 86±7 | 45±27 | 61 |
| UL_PUR | NCA/graphite | 3.4 | 2.7-4.2 | 209±50 | 89±6 | 41±33 | 10 |

For RUL (Remaining Useful Life) tasks, we also created combined datasets from the public sources to assess training efficacy when various battery data are combined. Notably:
- CRUH combines CALCE, RWTH, UL_PUR, and HNEI datasets
- CRUSH merges CALCE, RWTH, UL_PUR, SNL, and HNEI datasets
- MIX incorporates all datasets used in our study.

For more detailed information on the data, please refer to the Appendix A of our paper.

RUL(잔여 사용 수명) 작업의 경우, 다양한 배터리 데이터를 결합했을 때 학습 효과를 평가하기 위해 <br> 공개 소스에서 결합된 데이터 세트도 만들었습니다.
주목할 만한 점은
 -  CRUH는 CALCE, RWTH, UL_PUR 및 HNEI 데이터 세트를 결합합니다.
 -  CRUSH는 CALCE, RWTH, UL_PUR, SNL 및 HNEI 데이터 세트를 병합합니다.
 -  MIX는 연구에 사용된 모든 데이터 세트를 통합합니다.

데이터에 대한 자세한 내용은 백서의 부록 A를 참조하세요.

## Benchmark result of RUL(Remain Useful Life) task
Benchmark results for remaining useful life prediction. The comparison methods are split into four types, including
1) dummy regressor, a trivial baseline that uses the mean of training label as predictions;
2) linear models with features designed by domain experts;
3) traditional statistical models with *QdLinear* feature;
4) deep models with *QdLinear* feature.

For models sensitive to initialization, we present the error mean across ten seeds and attach the standard deviation as subscript.

잔여 유효 수명 예측에 대한 벤치마크 결과.<br>
비교 방법은 다음과 같은 네 가지 유형으로 나뉩니다.

훈련 레이블의 평균을 예측값으로 사용하는 간단한 기준선인 dummy regressor;
도메인 전문가가 설계한 기능을 갖춘 linear models;
QdLinear 기능이 있는 traditional statistical models ;
QdLinear 기능을 갖춘 deep model.

초기화에 민감한 모델의 경우, 10개 시드에 대한 오차 평균을 제시하고 표준 편차를 아래 첨자로 첨부합니다.


| **Models**     | **MATR1** | **MATR2** | **HUST** | **SNL** | **CLO** | **CRUH** | **CRUSH** | **MIX** |
|----------------|-----------|-----------|----------|---------|---------|----------|-----------|---------|
| Dummy regressor|398        |510        |419       |466      |331      |239       |576        |573      |
| "Variance" model|136       |211        |398       |360      |179      |118       |506        |521      |
| "Discharge" model|329      |**149**    |**322**   |267      |143      |76        |>1000    |>1000  |
| "Full" model   |167        |>1000    |335       |433      |**138**  |93        |>1000    |331      |
| Ridge regression|116       |184        |>1000   |242      |169      |65        |>1000    |372      |
| PCR            |**90**    |187        |435       |**200**  |197      |68        |560        |376      |
| PLSR           |104        |181        |431       |242      |176      |**60**    |535        |383      |
| Gaussian process|154       |224        |>1000   |251      |204      |115       |>1000    |573      |
| XGBoost        |334        |799        |395       |547      |215      |119       |**330**    |205      |
| Random forest  |168±9      |233±7      |368±7     |532±25   |192±2    |81±1      |416±5      |**197±0**|
| MLP            |149±3      |275±27     |459±9     |370±81   |146±5    |103±4     |565±9      |451±42   |
| CNN            |102±94     |228±104    |465±75    |924±267  |>1000  |174±92    |545±11     |272±101  |
| LSTM           |119±11     |219±33     |443±29    |539±40   |222±12   |105±10    |519±39     |268±9    |
| Transformer    |135±13     |364±25     |391±11    |424±23   |187±14   |81±8      |550±21     |271±16   |



## Quick Start

### Install

```shell
pip install -r requirements.txt
pip install .

pip install -e .
```

This will install the BatteryML into your Python environment, together with a convenient command line interface (CLI) `batteryml`.
You may also need to [install PyTorch](https://pytorch.org/get-started/locally/) for deep models.

이렇게 하면 편리한 명령줄 인터페이스(CLI) batteryml과 함께 Python 환경에 BatteryML이 설치됩니다. 딥 모델을 위해 PyTorch를 설치해야 할 수도 있습니다.

### Download Raw Data and Run Preprocessing Scripts
<!-- Download the raw data and execute the preprocessing scripts as per the provided [instruction](./dataprepare.md). You can also use the code below to download public datasets and convert them to BatteryML's uniform data format. -->
Download raw files of public datasets and preprocess them into `BatteryData` of BatteryML is now as simple as two commands:

```bash
batteryml download MATR /path/to/save/raw/data
batteryml preprocess MATR /path/to/save/raw/data /path/to/save/processed/data
```

### Run Cycler Preprocessing Scripts to process your data
If your data is measured by a cycler such as ARBIN, NEWARE, etc., you can use this command to process your data into `BatteryData` of BatteryML.

```bash
batteryml preprocess ARBIN /path/to/save/raw/data /path/to/save/processed/data --config /path/to/config/yaml/file
```

Due to variations in software versions and configurations, the data format and fields exported by the same cycler may differ. Therefore, we have added default processing configurations in the `/configs/cycler` directory to map raw data to target data fields. You can edit these default configurations as needed.

We currently support `ARBIN` and `NEWARE` data formats. Additionally, `Biologic`, `LANDT`, and `Indigo` formats are being integrated.  If you encounter any issues with our cycler processing your data, please submit an issue and attach a sample data file to help us ensure rapid compatibility with your data format.

소프트웨어 버전과 구성의 차이로 인해 동일한 사이클러에서 내보내는 데이터 형식과 필드가 다를 수 있습니다. 따라서 raw data를 target data fields에 매핑하기 위해 /configs/cycler 디렉터리에 기본 처리 구성을 추가했습니다. 필요에 따라 이러한 기본 구성을 편집할 수 있습니다.

현재 지원되는 데이터 형식은 ARBIN과 NEWARE입니다. 또한 Biologic, LANDT, Indigo 형식도 통합 중입니다. 싸이클러가 데이터를 처리하는 데 문제가 발생하면 문제를 제출하고 샘플 데이터 파일을 첨부하여 데이터 형식과의 신속한 호환성을 보장할 수 있도록 도와주세요.

### Run training and/or inference tasks using config files

BatteryML supports using a simple config file to specify the training and inference process. We provided several examples in `configs`. For example, to reproduce the "variance" model for battery life prediction, run

BatteryML은 간단한 설정 파일을 사용하여 학습 및 추론 프로세스를 지정할 수 있도록 지원합니다. 'config'에 몇 가지 예제를 제공했습니다. 예를 들어 배터리 수명 예측을 위한 '분산' 모델을 재현하려면 다음을 실행합니다.

```bash
batteryml run configs/baselines/sklearn/variance_model/matr_1.yaml ./workspace/test --train --eval
```


## Citation

If you find this work useful, we would appreciate citations to the following paper:
```
@inproceedings{zhang2024batteryml,
  title={Battery{ML}: An Open-source Platform for Machine Learning on Battery Degradation},
  author={Han Zhang and Xiaofan Gui and Shun Zheng and Ziheng Lu and Yuqi Li and Jiang Bian},
  booktitle={The Twelfth International Conference on Learning Representations},
  year={2024}
}
```

## Documentation

By leveraging BatteryML, researchers can gain valuable insights into the latest advancements in battery prediction and materials science, enabling them to conduct experiments efficiently and effectively. We invite you to join us in our journey to accelerate battery research and innovation by contributing to and utilizing BatteryML for your research endeavors.
