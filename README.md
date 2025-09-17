# M3info
Sample ID または Coustomer ID から検体情報を取得する。\
※**データベースの設計内容が不明なため、データベース検索時に想定外の動作を行う可能性があります。**\
表示される検体情報の各項目は以下のとおり。
| 項目             | 内容              |verbose |
|:-----------------|:------------------|:-------|
|SAMPLE_ID         |Sample ID          |        |
|PATIENT_NO        |Patient ID         |        |
|Specimen_ID       |Specimen ID        | True   |
|BATCH             |バッチフォルダ名   |        |
|GENDER            |性別               | True   |
|BIRTH_DATE        |生年月日           | True   |
|AGE               |年齢               | True   |
|SAMPLING_DATE     |検体採取日         | True   |
|DIAGNOSIS_NAME    |疾患名             |        |
|OCCURRED_ORGAN    |採取部位           | True   |
|BIOPSY_OR_SURGERY |生検または手術検体 | True   |
|Clinician         |担当医師名         | True   |
|Institution       |施設名             |        |
|Title             |臨床試験名         | True   |
|Cohort            |コホート           |        |
|Timepoint         |タイムポイント     | True   |
|ANAL_STATUS       |解析ステータス     |        |
|REPORT_DATE       |レポート返却日     | True   |

## エイリアスの作成 ※ 初回のみ
~/bin フォルダ直下に以下のコマンドを記載したテキストファイル M3info を作成し、実行権限を付与する。\
（gxd_pipeline, guest_user ユーザーには実装済み）\
エイリアスを作成しない場合は、singularity でコンテナとスクリプトファイルを指定して実行する。
```
singularity exec --disable-cache --bind /data1 /data1/labTools/labTools.sif python /data1/labTools/M3info/latest/M3info.py $@
```
helpページを表示してエイリアスの設定を確認する。以下が表示されればOK。
```
$ M3info --help
version: v1.1.0
usage: M3info.py [-h] [--sample_id SAMPLE_ID] [--patient_id PATIENT_ID] 
                 [--verbose] [--directory DIRECTORY] [--version]

optional arguments:
  -h, --help            show this help message and exit
  --sample_id SAMPLE_ID, -s SAMPLE_ID
                        sample id (default: None)
  --patient_id PATIENT_ID, -p PATIENT_ID
                        Patient ID (default: None)
  --verbose             Show details (default: False)
  --directory DIRECTORY, -d DIRECTORY
                        parent analytical directory (default: /data1/data/result)
  --version, -v         show program's version number and exit
```

## 1\. Sample ID で検索
```
M3info --sample_id <sample ID>
M3info -s <sample ID>
```

## 2\. patient ID で検索
```
M3info --patient_id <patient ID>
M3info -p <patient ID>
```
