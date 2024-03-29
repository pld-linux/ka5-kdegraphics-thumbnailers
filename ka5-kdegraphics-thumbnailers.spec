#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.5
%define		kframever	5.103.0
%define		qtver		5.15.2
%define		kaname		kdegraphics-thumbnailers
Summary:	KDE graphics thumbnailers
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	a04dfe3a1626ffa57304cc8c6eb4b16c
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	ka5-kdegraphics-mobipocket-devel >= %{kdeappsver}
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
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/thumbcreator/blenderthumbnail.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/thumbcreator/gsthumbnail.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/thumbcreator/mobithumbnail.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/thumbcreator/rawthumbnail.so
%{_datadir}/metainfo/org.kde.kdegraphics-thumbnailers.metainfo.xml
