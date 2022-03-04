%define		kdeappsver	21.12.3
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kdegraphics-thumbnailers
Summary:	KDE graphics thumbnailers
Name:		ka5-%{kaname}
Version:	21.12.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	88d98a7bce5ed8e1d51884fa0be99a50
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
Te wtyczki pozwalają oprogramowaniu KDE tworzyć miniaturki dla
wielu zaawansowanych formatów graficznych (PS, RAW).

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

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
