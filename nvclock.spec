Summary:	NVidia overclock utility
Summary(pl):	Narzêdzie do podkrêcania kart NVidii
Name:		nvclock
Version:	0.7
Release:	3
License:	GPL
Group:		Applications/System
Source0:	http://www.linuxhardware.org/nvclock/%{name}%{version}.tar.gz
# Source0-md5:	a3bb5ff1c2638317f1a69c7c2442b9e4
Source1:	%{name}.png
Source2:	%{name}.desktop
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.linuxhardware.org/nvclock/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	qt-devel
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
Summary:	GTK version of nvclock
Summary(pl):	nvclock z interfejsem GTK
Group:		Applications/System
Requires:	%{name}-common = %{version}-%{release}

%description gtk
This program allows you to overclock your NVidia card under linux.

Warning! It can burn your graphics card!

This is GTK version.

%description gtk -l pl
Ten program pozwala na podkrêcanie karty graficznej NVidia pod
Linuksem.

Uwaga! Mo¿e on spaliæ kartê graficzn±!

To jest wersja GTK.

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
	--enable-qt
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
