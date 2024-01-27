[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android U

1. 修改 `vendor/mediatek/proprietary/packages/apps/SoundRecorderOP01/src/com/android/soundrecorder/RecordingFileList.java` 类中 `queryData()` 方法的如下代码：

   ```diff
   @@ -411,6 +411,81 @@ public class RecordingFileList extends Activity implements ImageButton.OnClickLi
                    }
                });
                e.printStackTrace();
   +        } finally {
   +            if (null != recordingFileCursor) {
   +                recordingFileCursor.close();
   +                recordingFileCursor = null;
   +            }
   +        }
   +        
   +        where = MediaStore.Video.Media.DATA + " LIKE ?";
   +        recordingFileCursor = getContentResolver().query(
   +                MediaStore.Video.Media.EXTERNAL_CONTENT_URI,
   +                new String[] {
   +                        MediaStore.Video.Media.ARTIST, MediaStore.Video.Media.ALBUM,
   +                        MediaStore.Video.Media.DATA, MediaStore.Video.Media.DURATION,
   +                        MediaStore.Video.Media.DISPLAY_NAME, MediaStore.Video.Media.DATE_ADDED,
   +                        MediaStore.Video.Media.TITLE, MediaStore.Video.Media._ID
   +                }, where, new String[] {"%Recordings/record%.3gpp"}, null);
   +        try {
   +            if ((null == recordingFileCursor) || (0 == recordingFileCursor.getCount())) {
   +                LogUtils.i(TAG, "<queryVideData> the data return by query is null");
   +                return mArrlist;
   +            }
   +            LogUtils.i(TAG, "<queryVideoData> the data return by query is available");
   +            recordingFileCursor.moveToFirst();
   +            int num = recordingFileCursor.getCount();
   +            final int sizeOfHashMap = 6;
   +            String path = null;
   +            String fileName = null;
   +            int duration = 0;
   +            long cDate = 0;
   +            SimpleDateFormat simpleDateFormat = new SimpleDateFormat(getResources().getString(
   +                        R.string.audio_db_title_format));
   +            String createDate = null;
   +            int recordId = 0;
   +            Date date = new Date();
   +            for (int j = 0; j < num; j++) {
   +                HashMap<String, Object> map = new HashMap<String, Object>(sizeOfHashMap);
   +                path = recordingFileCursor.getString(PATH_INDEX);
   +                if (null != path) {
   +                    fileName = path.substring(path.lastIndexOf("/") + 1, path.length());
   +                }
   +                duration = recordingFileCursor.getInt(DURATION_INDEX);
   +                if (duration < ONE_SECOND) {
   +                    duration = ONE_SECOND;
   +                }
   +                cDate = recordingFileCursor.getInt(CREAT_DATE_INDEX);
   +                date.setTime(cDate * ONE_SECOND);
   +                createDate = simpleDateFormat.format(date);
   +                recordId = recordingFileCursor.getInt(RECORD_ID_INDEX);
   +
   +                map.put(FILE_NAME, fileName);
   +                map.put(PATH, path);
   +                map.put(DURATION, duration);
   +                map.put(CREAT_DATE, createDate);
   +                map.put(FORMAT_DURATION, formatDuration(duration));
   +                map.put(RECORD_ID, recordId);
   +
   +                mNameList.add(fileName);
   +                mPathList.add(path);
   +                mTitleList.add(createDate);
   +                mDurationList.add(formatDuration(duration));
   +                mIdList.add(recordId);
   +
   +                recordingFileCursor.moveToNext();
   +                mArrlist.add(map);
   +            }
   +        } catch (IllegalStateException e) {
   +            mHandler.post(new Runnable() {
   +                @Override
   +                public void run() {
   +                    ErrorHandle
   +                    .showErrorInfo(RecordingFileList.this,
   +                                                 ErrorHandle.ERROR_ACCESSING_DB_FAILED_WHEN_QUERY);
   +                }
   +            });
   +            e.printStackTrace();
            } finally {
                if (null != recordingFileCursor) {
                    recordingFileCursor.close();
   ```

2. 修改 `vendor/mediatek/proprietary/packages/apps/SoundRecorderOP01/src/com/android/soundrecorder/SoundRecorderUtils.java` 文件中 `deleteFileFromMediaDB()` 方法的如下代码：

   ```diff
   @@ -105,11 +105,39 @@ public class SoundRecorderUtils {
                    LogUtils.i(TAG, "<deleteFileFromMediaDB> delete " + deleteNum + " items in db");
                    res = (deleteNum != 0);
                } else {
   -                if (cursor == null) {
   -                    LogUtils.e(TAG, "<deleteFileFromMediaDB>, cursor is null");
   +                if (filePath.endsWith(".3gpp")) {
   +                    if (null != cursor) {
   +                        cursor.close();
   +                        cursor = null;
   +                    }
   +                    base = MediaStore.Video.Media.EXTERNAL_CONTENT_URI;
   +                    final String[] vids = new String[] { MediaStore.Video.Media._ID };
   +                    StringBuilder sb = new StringBuilder();
   +                    sb.append(MediaStore.Video.Media.DATA);
   +                    sb.append(" LIKE '%");
   +                    sb.append(filePath.replaceFirst("file:///", ""));
   +                    sb.append("'");
   +                    final String vwhere = sb.toString();
   +                    cursor = query(context, base, vids, vwhere, null, null);
   +                    if ((null != cursor) && (cursor.getCount() > 0)) {
   +                        int deleteNum = resolver.delete(base, where, null);
   +                        LogUtils.i(TAG, "<deleteFileFromMediaDB> delete " + deleteNum + " items in db");
   +                        res = (deleteNum != 0);
   +                    } else {
   +                        if (cursor == null) {
   +                            LogUtils.e(TAG, "<deleteFileFromMediaDB>, cursor is null");
   +                        } else {
   +                            LogUtils.e(TAG, "<deleteFileFromMediaDB>, cursor is:" + cursor
   +                                    + "; cursor.getCount() is:" + cursor.getCount());
   +                        }
   +                    }
                    } else {
   -                    LogUtils.e(TAG, "<deleteFileFromMediaDB>, cursor is:" + cursor
   -                            + "; cursor.getCount() is:" + cursor.getCount());
   +                    if (cursor == null) {
   +                        LogUtils.e(TAG, "<deleteFileFromMediaDB>, cursor is null");
   +                    } else {
   +                        LogUtils.e(TAG, "<deleteFileFromMediaDB>, cursor is:" + cursor
   +                                + "; cursor.getCount() is:" + cursor.getCount());
   +                    }
                    }
                }
            } catch (IllegalStateException e) {
   ```

   