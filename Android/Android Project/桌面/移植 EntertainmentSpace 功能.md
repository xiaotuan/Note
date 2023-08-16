[toc]

### 1. MTK 

#### 1.1 MT8766

##### 1.1.1 Android T

1. 修改 `sys/packages/apps/Launcher3/src/com/android/launcher3/Launcher.java` 文件中如下代码：

   ```diff
   @@ -232,6 +232,10 @@ import java.util.function.Predicate;
    import java.util.function.Supplier;
    import java.util.stream.Stream;
    
   +// Add the EntertainmentSpace feature by qty {{&&
   +import com.google.android.mediahome.launcheroverlay.client.PeekyTab;
   +// &&}}
   +
    /**
     * Default launcher application.
     */
   @@ -386,6 +390,10 @@ public class Launcher extends StatefulActivity<LauncherState>
        private LauncherState mPrevLauncherState;
    
        private StringCache mStringCache;
   +       
   +       // Add the EntertainmentSpace feature by qty {{&&
   +       private PeekyTab mPeekyTab;
   +       // &&}}
    
        @Override
        @TargetApi(Build.VERSION_CODES.S)
   @@ -533,6 +541,9 @@ public class Launcher extends StatefulActivity<LauncherState>
                mLauncherCallbacks.onCreate(savedInstanceState);
            }
            mOverlayManager = getDefaultOverlay();
   +               // Add the EntertainmentSpace feature by qty {{&&
   +               mOverlayManager.onActivityCreated(this, savedInstanceState);
   +               // &&}}
            PluginManagerWrapper.INSTANCE.get(this).addPluginListener(this,
                    LauncherOverlayPlugin.class, false /* allowedMultiple */);
    
   @@ -560,6 +571,19 @@ public class Launcher extends StatefulActivity<LauncherState>
        public OnboardingPrefs<? extends Launcher> getOnboardingPrefs() {
            return mOnboardingPrefs;
        }
   +       
   +       // Add the EntertainmentSpace feature by qty {{&&
   +       public View getPeekyTab(){
   +        if(this.mPeekyTab != null) {
   +            return this.mPeekyTab;
   +        }
   +        return null;
   +    }
   +
   +    public void setPeekyTab(PeekyTab peekyTab){
   +        this.mPeekyTab = peekyTab;
   +    }
   +       // &&}}
    
        @Override
        public void onPluginConnected(LauncherOverlayPlugin overlayManager, Context context) {
   ```

2. 修改 `sys/packages/apps/Launcher3/src/com/android/launcher3/allapps/AllAppsTransitionController.java` 文件中的如下代码：

   ```diff
   @@ -49,6 +49,11 @@ import com.android.launcher3.util.MultiValueAlpha;
    import com.android.launcher3.util.UiThreadHelper;
    import com.android.launcher3.views.ScrimView;
    
   +// Add the EntertainmentSpace feature by qty {{&&
   +import android.view.animation.AccelerateInterpolator;
   +import com.android.launcher3.folder.Folder;
   +// &&}}
   +
    /**
     * Handles AllApps view transition.
     * 1) Slides all apps view using direct manipulation
   @@ -63,6 +68,11 @@ public class AllAppsTransitionController
            implements StateHandler<LauncherState>, OnDeviceProfileChangeListener {
        // This constant should match the second derivative of the animator interpolator.
        public static final float INTERP_COEFF = 1.7f;
   +       
   +       // Add the EntertainmentSpace feature by qty {{&&
   +       private static final float PARALLAX_COEFFICIENT = .125f;
   +    private final Interpolator mAccelInterpolator = new AccelerateInterpolator(2f);
   +       // &&}}
    
        public static final FloatProperty<AllAppsTransitionController> ALL_APPS_PROGRESS =
                new FloatProperty<AllAppsTransitionController>("allAppsProgress") {
   @@ -190,6 +200,19 @@ public class AllAppsTransitionController
            mProgress = progress;
            getAppsViewProgressTranslationY().set(mAppsView, mProgress * mShiftRange);
            mLauncher.onAllAppsTransition(1 - progress);
   +               // Add the EntertainmentSpace feature by qty {{&&
   +               /*
   +               getAppsViewProgressTranslationY().set(mAppsView, mProgress * mShiftRange);
   +        mLauncher.onAllAppsTransition(1 - progress);
   +               */
   +               float shiftCurrent = progress * mShiftRange;
   +               View peekyTab = mLauncher.getPeekyTab();
   +        if (peekyTab != null) {
   +            peekyTab.setTranslationY(PARALLAX_COEFFICIENT * (-mShiftRange + shiftCurrent));
   +            float workspaceHotseatAlpha = Utilities.boundToRange(progress, 0f, 1f);
   +            peekyTab.setAlpha(mAccelInterpolator.getInterpolation(workspaceHotseatAlpha));
   +        }
   +               // &&}}
        }
    
        public float getProgress() {
   @@ -271,6 +294,7 @@ public class AllAppsTransitionController
         * Updates the property for the provided state
         */
        public void setAlphas(LauncherState state, StateAnimationConfig config, PropertySetter setter) {
   +        android.util.Log.d("qty", "[AllAppsTransitionController] setAlphas=>state: " + state + ", config: " + config + ", setter: " + setter);
            int visibleElements = state.getVisibleElements(mLauncher);
            boolean hasAllAppsContent = (visibleElements & ALL_APPS_CONTENT) != 0;
    
   @@ -281,6 +305,14 @@ public class AllAppsTransitionController
            boolean shouldProtectHeader =
                    ALL_APPS == state || mLauncher.getStateManager().getState() == ALL_APPS;
            mScrimView.setDrawingController(shouldProtectHeader ? mAppsView : null);
   +               
   +               // Add the EntertainmentSpace feature by qty {{&&
   +        boolean hasAnyVisibleItem = visibleElements != 0 && (visibleElements & LauncherState.OVERVIEW_ACTIONS) == 0 && (visibleElements & LauncherState.CLEAR_ALL_BUTTON) == 0;
   +               View peekyTab = mLauncher.getPeekyTab();
   +        if (peekyTab != null) {
   +            peekyTab.setVisibility(hasAnyVisibleItem ? View.VISIBLE:View.INVISIBLE);
   +        }
   +               // &&}}
        }
    
        public AnimatorListener getProgressAnimatorListener() {
   ```

3. 修改 `sys/packages/apps/Launcher3/Android.bp` 文件如下代码：

   ```diff
   @@ -19,6 +19,12 @@ package {
    
    min_launcher3_sdk_version = "26"
    
   +android_library_import {
   +    name: "mediahome-launcheroverlay",
   +    aars: ["libs/mediahome-launcheroverlay-1.1.0-eap.aar"],
   +    sdk_version: "current",
   +}
   +
    android_library {
        name: "launcher-aosp-tapl",
        libs: [
   @@ -305,6 +311,11 @@ android_library {
            "Launcher3CommonDepsLib",
            "QuickstepResLib",
            "SystemUIAnimationLib",
   +        "mediahome-launcheroverlay",
   +    ],
   +       aaptflags: [
   +        "--extra-packages",
   +        "com.google.android.apps.mediahome.launcher",
        ],
        manifest: "quickstep/AndroidManifest.xml",
        platform_apis: true,
   ```

4. 在 `sys/packages/apps/Launcher3/` 目录下创建 `libs` 目录，并将 `mediahome-launcheroverlay-1.1.0-eap.aar` 文件拖入其中。

5. 修改 `sys/vendor/partner_gms/apps/SearchLauncher/Android.mk` 文件中如下代码：

   ```diff
   @@ -66,6 +66,12 @@ LOCAL_STATIC_JAVA_LIBRARIES := \
        lib_launcherClient \
        SystemUISharedLib \
        SystemUI-statsd
   +       
   +LOCAL_STATIC_JAVA_AAR_LIBRARIES += mediahome-launcheroverlay
   +
   +LOCAL_AAPT_FLAGS := \
   +       --auto-add-overlay \
   +       --extra-packages com.google.android.apps.mediahome.launcher
    
    ifneq (,$(wildcard frameworks/base))
      LOCAL_PRIVATE_PLATFORM_APIS := true
   @@ -77,6 +83,7 @@ endif
    LOCAL_SRC_FILES := \
        $(call all-java-files-under, quickstep/src) \
        $(call all-java-files-under, src) \
   +    $(call all-java-files-under, $(LAUNCHER_PATH)/src)
    
    LOCAL_RESOURCE_DIR := \
        $(LOCAL_PATH)/quickstep/res \
   ```

6. 修改 `sys/vendor/partner_gms/apps/SearchLauncher/src/com/android/searchlauncher/OverlayCallbackImpl.java` 文件中如下代码：

   ```diff
   @@ -26,11 +26,27 @@ import com.android.launcher3.Utilities;
    import com.android.systemui.plugins.shared.LauncherOverlayManager;
    import com.android.systemui.plugins.shared.LauncherOverlayManager.LauncherOverlay;
    
   -import com.google.android.libraries.gsa.launcherclient.LauncherClient;
   -import com.google.android.libraries.gsa.launcherclient.LauncherClientCallbacks;
   +// Add EntertainmentSpace by qty {{&&
   +// import com.google.android.libraries.gsa.launcherclient.LauncherClient;
   +// import com.google.android.libraries.gsa.launcherclient.LauncherClientCallbacks;
   +// &&}}
    
    import java.io.PrintWriter;
    
   +// Add EntertainmentSpace by qty {{&&
   +import android.view.View.OnAttachStateChangeListener;
   +import android.view.ViewTreeObserver.OnGlobalLayoutListener;
   +import android.widget.FrameLayout;
   +import android.widget.FrameLayout.LayoutParams;
   +import android.os.Looper;
   +import com.google.android.mediahome.launcheroverlay.client.LauncherClient;
   +import com.google.android.mediahome.launcheroverlay.client.LauncherClientCallbacks;
   +import com.google.android.mediahome.launcheroverlay.common.AnimationType;
   +import com.google.android.mediahome.launcheroverlay.client.PeekyTab;
   +import android.view.View;
   +import android.view.LayoutInflater;
   +// &&}}
   +
    /**
     * Implements {@link LauncherOverlay} and passes all the corresponding events to {@link
     * LauncherClient}. {@see setClient}
   @@ -45,7 +61,13 @@ public class OverlayCallbackImpl
        public static final String KEY_ENABLE_MINUS_ONE = "pref_enable_minus_one";
    
        private final Launcher mLauncher;
   -    private final LauncherClient mClient;
   +       // Add EntertainmentSpace by qty {{&&
   +    // private final LauncherClient mClient;
   +       private  LauncherClient mClient;
   +       private final Looper mLooper = Looper.myLooper();
   +       private PeekyTab mPeekyTab;
   +       private OnGlobalLayoutListener peekyTabOnGlobalLayoutListener;
   +       // &&}}
    
        private LauncherOverlayCallbacks mLauncherOverlayCallbacks;
        private boolean mWasOverlayAttached = false;
   @@ -54,12 +76,29 @@ public class OverlayCallbackImpl
            SharedPreferences prefs = Utilities.getPrefs(launcher);
    
            mLauncher = launcher;
   -        mClient = new LauncherClient(mLauncher, this, getClientOptions(prefs));
   +               // Add EntertainmentSpace by qty {{&&
   +        // mClient = new LauncherClient(mLauncher, this, getClientOptions(prefs));
   +               // &&}}
            prefs.registerOnSharedPreferenceChangeListener(this);
        }
   +       
   +       // Add EntertainmentSpace by qty {{&&
   +       public View getPeekyTab() {
   +        return mPeekyTab;
   +    }
   + 
   +    public void adjustPeekyTabPosition() {
   +        if (mPeekyTab != null) {
   +            mPeekyTab.getViewTreeObserver().addOnGlobalLayoutListener(peekyTabOnGlobalLayoutListener);
   +        }
   +    }
   +       // &&}}
    
        @Override
        public void onDeviceProvideChanged() {
   +               // Add EntertainmentSpace by qty {{&&
   +               adjustPeekyTabPosition();
   +               // &&}}
            mClient.reattachOverlay();
        }
    
   @@ -75,22 +114,33 @@ public class OverlayCallbackImpl
    
        @Override
        public void dump(String prefix, PrintWriter w) {
   -        mClient.dump(prefix, w);
   +               // Add EntertainmentSpace by qty {{&&
   +        // mClient.dump(prefix, w);
   +               // &&}}
        }
    
        @Override
        public void openOverlay() {
   -        mClient.showOverlay(true);
   +               // Add EntertainmentSpace by qty {{&&
   +        // mClient.showOverlay(true);
   +               mClient.showOverlay(AnimationType.NONE,200);
   +               // &&}}
        }
    
        @Override
        public void hideOverlay(boolean animate) {
   -        mClient.hideOverlay(animate);
   +               // Add EntertainmentSpace by qty {{&&
   +        // mClient.hideOverlay(animate);
   +               mClient.hideOverlay(AnimationType.NONE,200);
   +               // &&}}
        }
    
        @Override
        public void hideOverlay(int duration) {
   -        mClient.hideOverlay(duration);
   +               // Add EntertainmentSpace by qty {{&&
   +        // mClient.hideOverlay(duration);
   +               mClient.hideOverlay(AnimationType.NONE,duration);
   +               // &&}}
        }
    
        @Override
   @@ -100,6 +150,51 @@ public class OverlayCallbackImpl
    
        @Override
        public void onActivityCreated(Activity activity, Bundle bundle) {
   +               // Add EntertainmentSpace by qty {{&&
   +               LayoutInflater.from(mLauncher)
   +                       .inflate(com.google.android.mediahome.launcheroverlay.R.layout.peeky_tab,
   +        mLauncher.findViewById(com.android.launcher3.R.id.drag_layer));
   +               mPeekyTab = mLauncher
   +                       .findViewById(com.google.android.mediahome.launcheroverlay.R.id.ohana_peeky_tab);
   +               mLauncher.setPeekyTab(mPeekyTab);                
   +               peekyTabOnGlobalLayoutListener = new OnGlobalLayoutListener() {
   +                       @Override
   +                       public void onGlobalLayout() {
   +                               // Adjust the position of the PeekyTab to make sure it doesn't collide with qsb.
   +                               View searchBar = mLauncher.findViewById(com.android.launcher3.R.id.search_container_workspace);
   +                               if (searchBar != null) {
   +                                       int[] location = new int[2];
   +                                       searchBar.getLocationOnScreen(location);
   +                                       int searchBarY = location[1];
   +                                       FrameLayout.LayoutParams params = (LayoutParams) mPeekyTab.getLayoutParams();
   +                                       // it has risks overlapping with search bar
   +                                       if (searchBarY > mPeekyTab
   +                                               .getPeekyTabDesignedHeight() +  mPeekyTab.getPeekyTabDesignedMarginTop()) {
   +                                               params.setMargins(0, mPeekyTab.getPeekyTabDesignedMarginTop() + 100, 0, 0);
   +                                       } else {
   +                                               if(searchBarY < 25) {
   +                                                       searchBarY= 56;
   +                                               }
   +                                               params.setMargins(0, searchBarY  + searchBar.getHeight() + 30, 0, 0);
   +                                       }
   +                                       mPeekyTab.setLayoutParams(params);
   +                               }
   +                               mPeekyTab.getViewTreeObserver().removeOnGlobalLayoutListener(this);
   +                       }
   +               };
   +               mPeekyTab.addOnAttachStateChangeListener(new OnAttachStateChangeListener() {
   +                       @Override
   +                       public void onViewAttachedToWindow(View v) { }
   + 
   +                       @Override
   +                       public void onViewDetachedFromWindow(View v) {
   +                               mPeekyTab.getViewTreeObserver().removeOnGlobalLayoutListener(peekyTabOnGlobalLayoutListener);
   +                       }
   +               });
   +               adjustPeekyTabPosition();
   + 
   +               mClient = new LauncherClient(mLauncher, mLooper, this,mPeekyTab); 
   +               // &&}}
            // Not called
        }
    
   @@ -110,12 +205,16 @@ public class OverlayCallbackImpl
    
        @Override
        public void onActivityResumed(Activity activity) {
   -        mClient.onResume();
   +               // Add EntertainmentSpace by qty {{&&
   +        // mClient.onResume();
   +               // &&}}
        }
    
        @Override
        public void onActivityPaused(Activity activity) {
   -        mClient.onPause();
   +               // Add EntertainmentSpace by qty {{&&
   +        // mClient.onPause();
   +               // &&}}
        }
    
        @Override
   @@ -135,12 +234,19 @@ public class OverlayCallbackImpl
        @Override
        public void onSharedPreferenceChanged(SharedPreferences prefs, String key) {
            if (KEY_ENABLE_MINUS_ONE.equals(key)) {
   -            mClient.setClientOptions(getClientOptions(prefs));
   +                       // Add EntertainmentSpace by qty {{&&
   +            //mClient.setClientOptions(getClientOptions(prefs));
   +                       // &&}}
            }
        }
   -
   +       
   +       // Add EntertainmentSpace by qty {{&&
   +       /*
        @Override
        public void onServiceStateChanged(boolean overlayAttached, boolean hotwordActive) {
   +       */
   +       @Override
   +    public void onServiceStateChanged(boolean overlayAttached) {
            if (overlayAttached != mWasOverlayAttached) {
                mWasOverlayAttached = overlayAttached;
                mLauncher.setLauncherOverlay(overlayAttached ? this : null);
   @@ -174,12 +280,13 @@ public class OverlayCallbackImpl
            mLauncherOverlayCallbacks = callbacks;
        }
    
   -
   -    private LauncherClient.ClientOptions getClientOptions(SharedPreferences prefs) {
   -        return new LauncherClient.ClientOptions(
   -                prefs.getBoolean(KEY_ENABLE_MINUS_ONE, true),
   -                true, /* enableHotword */
   -                true /* enablePrewarming */
   -        );
   -    }
   +       // Add EntertainmentSpace by qty {{&&
   +    // private LauncherClient.ClientOptions getClientOptions(SharedPreferences prefs) {
   +    //     return new LauncherClient.ClientOptions(
   +    //             prefs.getBoolean(KEY_ENABLE_MINUS_ONE, true),
   +    //             true, /* enableHotword */
   +    //             true /* enablePrewarming */
   +    //     );
   +    // }
   +       // &&}}
    }
   ```

7. 将 `EntrtainmentSpace` apk 文件拖入 `sys/vendor/partner_gms/apps/` 目录中。

8. 在 `sys/vendor/weibu_sz/products/products.mk` 文件中添加如下代码：

   ```diff
   PRODUCT_PACKAGES += EntertainmentSpace
   ```

   