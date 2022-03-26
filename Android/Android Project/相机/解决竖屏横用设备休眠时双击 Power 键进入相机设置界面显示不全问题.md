[toc]

### 1. MTK 平台

#### 1.1 MTK8766

##### 1.1.1 Android R

1. 修改 `vendor/mediatek/proprietary/packages/apps/Camera2/host/src/com/mediatek/camera/CameraActivity.java` 文件的如下代码：

   ```diff
   @@ -153,19 +153,18 @@ public class CameraActivity extends PermissionActivity implements IApp {
            //}
    
            //Add start by WB 20210924
   -        boolean isEnableOrientation = SystemProperties.getString("ro.surface_flinger.primary_display_orientation", "null").equals("ORIENTATION_90")
   -                                        | SystemProperties.getString("ro.surface_flinger.primary_display_orientation", "null").equals("ORIENTATION_270");
   -        boolean isOrientationFromLcm = SystemProperties.getInt("ro.surface_flinger.orientation_from_lcm",0)==1;
   +        // boolean isEnableOrientation = SystemProperties.getString("ro.surface_flinger.primary_display_orientation", "null").equals("ORIENTATION_90")
   +        //                                 | SystemProperties.getString("ro.surface_flinger.primary_display_orientation", "null").equals("ORIENTATION_270");
   +        // boolean isOrientationFromLcm = SystemProperties.getInt("ro.surface_flinger.orientation_from_lcm",0)==1;
    
   -        if(isEnableOrientation && isOrientationFromLcm){
   +        // if(isEnableOrientation && isOrientationFromLcm){
                   
   -            setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_LANDSCAPE);
   -        }else{
   -            setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_PORTRAIT);
   -        //    setRequestedOrientation(CameraUtil.calculateCurrentScreenOrientation(this));
   -        }
   +        //     setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_LANDSCAPE);
   +        // }else{
   +        //     setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_PORTRAIT);
   +        // //    setRequestedOrientation(CameraUtil.calculateCurrentScreenOrientation(this));
   +        // }
            //Add End 20210924
   -
            getWindow().getDecorView().setSystemUiVisibility(View.SYSTEM_UI_LAYOUT_FLAGS
                    | View.SYSTEM_UI_FLAG_LAYOUT_STABLE);
            CameraSysTrace.onEventSystrace("onCreateTasks.setContentView", true, true);
   ```

2. 修改 `vendor/mediatek/proprietary/packages/apps/Camera2/host/src/com/mediatek/camera/ui/CameraAppUI.java` 文件的如下所示：

   ```diff
   @@ -125,6 +125,8 @@ public class CameraAppUI implements IAppUi {
        private String mCurrentCameraId = "0";
        private String mCurrentModeType;
    
   +    private int mFirstDisplayRotation = 0;
   +
        private ModeProvider mModeProvider;
        private Handler mConfigUIHandler = new ConfigUIHandler();
        private static final int APPLY_ALL_UI_VISIBILITY = 0;
   @@ -146,6 +148,7 @@ public class CameraAppUI implements IAppUi {
         * Called when activity's onCreate() is invoked.
         */
        public void onCreate() {
   +        mFirstDisplayRotation = CameraUtil.getDisplayRotation(mApp.getActivity());
    
            ViewGroup rootView = (ViewGroup) mApp.getActivity()
                    .findViewById(R.id.app_ui_root);
   @@ -161,8 +164,8 @@ public class CameraAppUI implements IAppUi {
                FrameLayout.LayoutParams params =
                        (FrameLayout.LayoutParams) appUI.getLayoutParams();
                if (CameraUtil.isTablet()) {
   -                int displayRotation = CameraUtil.getDisplayRotation(mApp.getActivity());
   -               LogHelper.d(TAG, " onCreate displayRotation  " + displayRotation);
   +                int displayRotation = 0;//CameraUtil.getDisplayRotation(mApp.getActivity());
   +                LogHelper.d(TAG, " onCreate displayRotation  " + displayRotation);
                    if (displayRotation == 90 || displayRotation == 270) {
                        params.leftMargin += navigationBarHeight;
                        appUI.setLayoutParams(params);
   @@ -239,11 +242,11 @@ public class CameraAppUI implements IAppUi {
            hideAlertDialog();
            LogHelper.d(TAG, "onResume orientation = " + newConfig.orientation);
            if (root != null) {
   -            if (newConfig.orientation == Configuration.ORIENTATION_PORTRAIT) {
   +            // if (newConfig.orientation == Configuration.ORIENTATION_PORTRAIT) {
                    root.setOrientation(0, false);
   -            } else if (newConfig.orientation == Configuration.ORIENTATION_LANDSCAPE) {
   -                root.setOrientation(90, false);
   -            }
   +            // } else if (newConfig.orientation == Configuration.ORIENTATION_LANDSCAPE) {
   +            //     root.setOrientation(90, false);
   +            // }
            }
            //call each manager's onResume()
            for (int count = 0; count < mViewManagers.size(); count ++) {
   @@ -883,6 +886,8 @@ public class CameraAppUI implements IAppUi {
                    .findViewById(R.id.setting_ui_root);
    
            if (CameraUtil.isHasNavigationBar(mApp.getActivity())) {
   +            //get navigation bar height.
   +            int navigationBarHeight = CameraUtil.getNavigationBarHeight(mApp.getActivity());
                // Get the preview height don't contain navigation bar height.
                Point size = new Point();
                mApp.getActivity().getWindowManager().getDefaultDisplay().getSize(size);
   @@ -891,13 +896,18 @@ public class CameraAppUI implements IAppUi {
                        .findViewById(R.id.setting_container);
                LinearLayout.LayoutParams containerParams =
                        (LinearLayout.LayoutParams) settingContainer.getLayoutParams();
   -            containerParams.height = size.y;
   +            if (mFirstDisplayRotation != 0) {
   +                containerParams.height = (size.y > size.x ? size.y : size.x) - navigationBarHeight;
   +                containerParams.width = (size.x > size.y ? size.y : size.x) + navigationBarHeight;
   +            } else {
   +                containerParams.height = size.y;
   +            }
                settingContainer.setLayoutParams(containerParams);
    
                LinearLayout settingTail = (LinearLayout) settingRootView
                        .findViewById(R.id.setting_tail);
                //get navigation bar height.
   -            int navigationBarHeight = CameraUtil.getNavigationBarHeight(mApp.getActivity());
   +            // int navigationBarHeight = CameraUtil.getNavigationBarHeight(mApp.getActivity());
                LogHelper.d(TAG, "[layoutSettingUI], navigationBarHeight:" + navigationBarHeight);
                //set setting tail view height as navigation bar height.
   ```

   