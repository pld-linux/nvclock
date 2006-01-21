# TODO: security problem (/tmp/nvclock symlink attack possible)
Summary:	NVidia overclock utility
Summary(pl):	Narzêdzie do podkrêcania kart NVidii
Name:		nvclock
Version:	0.8b
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.linuxhardware.org/nvclock/%{name}%{version}.tar.gz
# Source0-md5:	a987c47e749a65922d7ff25817eda3b8
Source1:	%{name}.png
Source2:	%{name}.desktop
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.linuxhardware.org/nvclock/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.4.0
BuildRequires:	qt-devel >= 2.2.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.213
# I doubt if it works on anything other than x86 when it doesn't work on amd64...
ExcludeArch:	%{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		%{_sbindir}

%description
This program allows you to overclock your NVidia card under linux.

Warning! It can burn your graphics card!

%description -l pl
Ten program pozwala na podkrêcanie karty graficznej NVidia pod
Linuksem.

Uwaga! Mo¿e on spaliæ kartê graficzn±!

%package common
Summary:	Common files for different GUI versions of nvclock
Summary(pl):	Wspólne pliki dla ró¿nych wersji GUI nvclock
Group:		Applications/System

%description common
This package provides common files for different GUI versions of
nvclock.

%description common -l pl
Ten pakiet dostarcza wspólne pliki dla ró¿nych wersji interfejsu
graficznego programu nvclock.

%package gtk
Summary:	GTK+ version of nvclock
Summary(pl):	nvclock z interfejsem GTK+
Group:		Applications/System
Requires:	%{name}-common = %{version}-%{release}

%description gtk
This program allows you to overclock your NVidia card under linux.

Warning! It can burn your graphics card!

This is GTK+ version.

%description gtk -l pl
Ten program pozwala na podkrêcanie karty graficznej NVidia pod
Linuksem.

Uwaga! Mo¿e on spaliæ kartê graficzn±!

To jest wersja GTK+.

%package qt
Summary:	Qt version of nvclock
Summary(pl):	nvclock z interfejsem Qt
Group:		Applications/System
Requires:	%{name}-common = %{version}-%{release}

%description qt
This program allows you to overclock your NVidia card under linux.

Warning! It can burn your graphics card!

This is Qt version.

%description qt -l pl
Ten program pozwala na podkrêcanie karty graficznej NVidia pod
Linuksem.

Uwaga! Mo¿e on spaliæ kartê graficzn±!

To jest wersja Qt.

%prep
%setup -q -n %{name}%{version}
%patch0 -p1

%{__perl} -pi -e 's/-lqt/-lqt-mt/' src/qt/Makefile.in

%build
%{__aclocal}
%{__autoheader}
%{__autoconf}
%configure \
	--enable-gtk \
	--enable-qt \
	QT_LIB_DIR=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ABOUT AUTHORS ChangeLog FAQ README
%attr(755,root,root) %{_sbindir}/nvclock
%{_mandir}/man1/nvclock*

%files common
%defattr(644,root,root,755)
%{_pixmapsdir}/*
%{_desktopdir}/*

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/nvclock_gtk

%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/nvclock_qt
