[toc]

### 1. 展讯平台

#### 1.1. Android R

1. 修改 `frameworks\base\telephony\java\android\telephony\TelephonyManager.java` 文件，将 `getSimOperatorNameForPhone()` 方法：

   ```java
   public String getSimOperatorNameForPhone(int phoneId) {
       return getTelephonyProperty(phoneId, TelephonyProperties.icc_operator_alpha(), "");
   }
   ```

   修改成：

   ```java
   public String getSimOperatorNameForPhone(int phoneId) {
       String operator = getSimOperatorNumericForPhone(phoneId);
       if (operator != null) {
           if ("60201".equals(operator)) {
               return "Orange";
           } else if ("60202".equals(operator)) {
               return "Vodafone";
           } else if ("60203".equals(operator)) {
               return "Etisalat";
           } else if ("60204".equals(operator)) {
               return "TE/WE";
           } else if ("46001".equals(operator)) {
               return "Lucky";
           }
       }
       return getTelephonyProperty(phoneId, TelephonyProperties.icc_operator_alpha(), "");
   }
   ```

2. 修改 `frameworks\base\telephony\java\android\telephony\SubscriptionInfo.java` 文件，将 `getCarrierName()` 方法：

   ```java
   public CharSequence getCarrierName() {
       return this.mCarrierName;
   }
   ```

   修改成：

   ```java
   public CharSequence getCarrierName() {
       if ("602".equals(this.mMcc)) {
           if ("01".equals(this.mMnc)) {
               return "Orange";
           } else if ("02".equals(this.mMnc)) {
               return "Vodafone";
           } else if ("03".equals(this.mMnc)) {
               return "Etisalat";
           } else if ("04".equals(this.mMnc)) {
               return "TE/WE";
           }
       } else if ("460".equals(this.mMcc) && "01".equals(this.mMnc)) {
           return "Lucky";
       }
       return this.mCarrierName;
   }
   ```

   

