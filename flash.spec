Name: flash
Version: 24.0.0.194
Release: 1%{?dist}
Summary: Flash plugin importer
Summary(ar): مستورد إضافة فلاش
License: Commerical
URL: https://github.com/moceap/flash
Source0: README.md
Obsoletes: flash-plugin
Provides: flash-plugin
Requires: freshplayerplugin
Requires: wget

%description
Importing Flash plugin from Adobe as Pepper to Firefox and Chromium and others.

Flash player is regestered mark of Adobe.

%description -l ar
جلب إضافة فلاش من كإضافة بيبر لاستخدامها في فيرفكس وكروميوم وغيرهما.

فلاش بلير علامة مسجلة لأدوبي.
%prep
cp -p %{SOURCE0} %{_builddir}

%post
%ifarch %{ix86}
if [ -e /tmp/flash ]
then rm -rf /tmp/flash
fi
mkdir /tmp/flash
wget -O /tmp/flash/flash_player_ppapi_linux.i386.tar.gz https://fpdownload.adobe.com/pub/flashplayer/pdc/%{version}/flash_player_ppapi_linux.i386.tar.gz
pushd /tmp/flash
tar -zxvf flash_player_ppapi_linux.i386.tar.gz
mkdir -p %{_libdir}/chromium-browser/PepperFlash
mkdir -p %{_datadir}/licenses/flash
cp -p libpepflashplayer.so manifest.json %{_libdir}/chromium-browser/PepperFlash
cp -pr readme.txt license.pdf LGPL %{_datadir}/licenses/flash
popd
rm -rf /tmp/flash
%endif
%ifarch x86_64
if [ -e /tmp/flash ]
then rm -rf /tmp/flash
fi
mkdir /tmp/flash
wget -O /tmp/flash/flash_player_ppapi_linux.x86_64.tar.gz https://fpdownload.adobe.com/pub/flashplayer/pdc/%{version}/flash_player_ppapi_linux.x86_64.tar.gz
pushd /tmp/flash
tar -zxvf flash_player_ppapi_linux.x86_64.tar.gz
mkdir -p %{_libdir}/chromium-browser/PepperFlash
mkdir -p %{_datadir}/licenses/flash
cp -p libpepflashplayer.so manifest.json %{_libdir}/chromium-browser/PepperFlash
cp -pr readme.txt license.pdf LGPL %{_datadir}/licenses/flash
popd
rm -rf /tmp/flash
%endif

%preun
if [ $1 = 0 ] ; then
rm %{_libdir}/chromium-browser/PepperFlash/manifest.json
rm %{_libdir}/chromium-browser/PepperFlash/libpepflashplayer.so
rm -rf %{_datadir}/licenses/flash
fi

%files
%doc README.md

%changelog
* Fri Feb 3 2017 Mosaab Alzoubi <moceap@hotmail.com> - 24.0.0.194-1
- Updated to 24.0.0.194

* Sun Dec 18 2016 Mosaab Alzoubi <moceap@hotmail.com> - 24.0.0.186-2
- Fix unstart after updating
- Add wget as require

* Fri Dec 16 2016 Mosaab Alzoubi <moceap@hotmail.com> - 24.0.0.186-1
- Updated to 24.0.0.186

* Sat Nov 26 2016 Mosaab Alzoubi <moceap@hotmail.com> - 23.0.0.207-1
- TEST build
