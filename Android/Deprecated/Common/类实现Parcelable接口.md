范例：

```java
import android.os.Parcel;
import android.os.Parcelable;

public class PassRecord implements Parcelable {

    /**
     * 人员编号，必选
     */
    public int person_id;
    /**
     * 人员类型，可选，0：部门人员、1：访客、2：黑名单、3：教师
     */
    public int person_type;
    /**
     * 流水 id 号，必选
     */
    public int pass_id;
    /**
     * 权限编号，必选
     */
    public int auth_id;
    /**
     * 过闸时间点，必选
     */
    public String pass_ts;
    /**
     * 设备端本地保存的比对阈值，必选
     */
    public float default_face_feature_rate;
    /**
     * 本次比对后的阈值，必选
     */
    public float current_face_feature_rate;
    /**
     * 设备端剩余的过闸次数，必选
     */
    public int count;
    /**
     * 性别，必选
     */
    public int gender;
    /**
     * 出生日期，必选
     */
    public String birthday;
    /**
     *身份证地址，必选
     */
    public String location;
    /**
     * 签发日期，必选
     */
    public String validity_time;
    /**
     * 签发机关，必选
     */
    public String signing_organization;
    /**
     * 民族，必选
     */
    public String nation;
    /**
     * 身份证号码，必选
     */
    public String id_number;
    /**
     * 名称，必选
     */
    public String name;
    /**
     * 身份证照片，base64 编码图像文件，可选
     */
    public String id_img;
    /**
     * 过闸时照片，base64 编码图像文件，可选
     */
    public String now_img;

    public PassRecord() {

    }

    private PassRecord(Parcel in) {
        person_id = in.readInt();
        person_type = in.readInt();
        pass_id = in.readInt();
        auth_id = in.readInt();
        pass_ts = in.readString();
        default_face_feature_rate = in.readFloat();
        current_face_feature_rate = in.readFloat();
        count = in.readInt();
        gender = in.readInt();
        birthday = in.readString();
        location = in.readString();
        validity_time = in.readString();
        signing_organization = in.readString();
        nation = in.readString();
        id_number = in.readString();
        name = in.readString();
        id_img = in.readString();
        now_img = in.readString();
    }

    @Override
    public int describeContents() {
        return 0;
    }

    @Override
    public void writeToParcel(Parcel out, int flags) {
        out.writeInt(person_id);
        out.writeInt(person_type);
        out.writeInt(pass_id);
        out.writeInt(auth_id);
        out.writeString(pass_ts);
        out.writeFloat(default_face_feature_rate);
        out.writeFloat(current_face_feature_rate);
        out.writeInt(count);
        out.writeInt(gender);
        out.writeString(birthday);
        out.writeString(location);
        out.writeString(validity_time);
        out.writeString(signing_organization);
        out.writeString(nation);
        out.writeString(id_number);
        out.writeString(name);
        out.writeString(id_img);
        out.writeString(now_img);
    }

    public static final Parcelable.Creator<PassRecord> CREATOR = new Parcelable.Creator<PassRecord>() {

        @Override
        public PassRecord createFromParcel(Parcel source) {
            return new PassRecord(source);
        }

        @Override
        public PassRecord[] newArray(int size) {
            return new PassRecord[size];
        }
    };
}
```

