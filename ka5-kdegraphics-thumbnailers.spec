#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.08.3
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kdegraphics-thumbnailers
Summary:	KDE graphics thumbnailers
Name:		ka5-%{kaname}
Version:	22.08.3
Release:	2
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	82bc592fd90d9f096a51577463545403
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	ka5-libkdcraw-devel >= %{kdeappsver}
BuildRequires:	ka5-libkexiv2-devel >= %{kdeappsver}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These plugins allow KDE software to create thumbnails for several
advanced graphic file formats (PS, RAW).

%description -l pl.UTF-8
Te wtyczki pozwalają oprogramowaniu KDE tworzyć miniaturki dla wielu
zaawansowanych formatów graficznych (PS, RAW).

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt5/plugins/blenderthumbnail.so
%attr(755,root,root) %{_libdir}/qt5/plugins/gsthumbnail.so
%attr(755,root,root) %{_libdir}/qt5/plugins/rawthumbnail.so
%{_datadir}/kservices5/blenderthumbnail.desktop
%{_datadir}/kservices5/gsthumbnail.desktop
%{_datadir}/kservices5/rawthumbnail.desktop
%{_datadir}/metainfo/org.kde.kdegraphics-thumbnailers.metainfo.xml
%attr(755,root,root) %{_libdir}/qt5/plugins/mobithumbnail.so
%{_datadir}/kservices5/mobithumbnail.desktop
