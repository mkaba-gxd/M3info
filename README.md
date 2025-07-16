# M3info
Sample ID または Coustomer ID から検体情報を取得する。\
表示される検体情報の各項目は以下の通り。
| 項目             | 内容              |
|:-----------------|:------------------|
|SAMPLE_ID         |Sample ID          |
|PATIENT_NO        |Patient ID         |
|BATCH             |バッチフォルダ名   |
|GENDER            |性別               |
|BIRTH_DATE        |生年月日           |
|AGE               |年齢               |
|SAMPLING_DATE     |検体採取日         |
|DIAGNOSIS_NAME    |疾患名             |
|OCCURRED_ORGAN    |採取部位           |
|BIOPSY_OR_SURGERY |生検または手術検体 |
|Clinician         |依頼医師名         |
|Institution       |施設名             |
|Cohort            |コホート           |
|Timepoint         |タイムポイント     |

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
version: v1.0.0
usage: M3info.py [-h] [--version] {sample_ID,sid,patient_ID,pid} ...

Search the database for specimen information.

positional arguments:
  {sample_ID,sid,patient_ID,pid}
    sample_ID (sid)     Search by sample ID
    patient_ID (pid)    Search by Patient ID

optional arguments:
  -h, --help            show this help message and exit
  --version, -v         show program's version number and exit
```
コマンド別の詳細表示
```
M3info <command> --help
```
## 1\. Sample ID で検索
```
M3info sample_ID --sample_id <sample ID>
M3info sid -s <sample ID>
```

## 2\. patient ID で検索
```
M3info patient_ID --patient_id <patient ID>
M3info pid -p <patient ID>
```
