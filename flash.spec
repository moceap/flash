Name: ojuba-flash
Version: 23.0.0.207
Release: 1%{?dist}
Summary: Adobe Flash Player for Ojuba
Summary(ar): أدوبي فلاش بلير لأعجوبة
License: Commerical
URL: https://github.com/ojuba-org/ojuba-flash
Source: README.md
Obsoletes: flash-plugin
Provides: flash-plugin
Requires: freshplayerplugin

%description
Adobe Flash Player for Ojuba.

Flash player is regestered mark of Adobe.

%description -l ar
أدوبي فلاش بلير لأعجوبة.

فلاش بلير علامة مسجلة لأدوبي.
%post
%ifarch %{ix86}
if [ -e /tmp/ojuba-flash ]
then rm -rf /tmp/ojuba-flash
fi
mkdir /tmp/ojuba-flash
wget -O /tmp/ojuba-flash/flash_player_ppapi_linux.i386.tar.gz https://fpdownload.adobe.com/pub/flashplayer/pdc/%{version}/flash_player_ppapi_linux.i386.tar.gz
pushd /tmp/ojuba-flash
tar -zxvf flash_player_ppapi_linux.i386.tar.gz
mkdir -p %{_libdir}/chromium-browser/PepperFlash
cp -p libpepflashplayer.so manifest.json %{_libdir}/chromium-browser/PepperFlash
popd
rm -rf /tmp/ojuba-flash
%endif
%ifarch x86_64
if [ -e /tmp/ojuba-flash ]
then rm -rf /tmp/ojuba-flash
fi
mkdir /tmp/ojuba-flash
wget -O /tmp/ojuba-flash/flash_player_ppapi_linux.x86_64.tar.gz https://fpdownload.adobe.com/pub/flashplayer/pdc/%{version}
pushd /tmp/ojuba-flash
tar -zxvf flash_player_ppapi_linux.x86_64.tar.gz
mkdir -p %{_libdir}/chromium-browser/PepperFlash
cp -p libpepflashplayer.so manifest.json %{_libdir}/chromium-browser/PepperFlash
popd
rm -rf /tmp/ojuba-flash
%endif

%postun
rm %{_libdir}/chromium-browser/PepperFlash/manifest.json
rm %{_libdir}/chromium-browser/PepperFlash/libpepflashplayer.so

%files
%doc README.md

%changelog
* Sat Nov 26 2016 Mosaab Alzoubi <moceap@hotmail.com> - 23.0.0.207-1
- TEST build
