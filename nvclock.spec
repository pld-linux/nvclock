Summary:	nvidia overclock utility
Summary(pl):	Narzêdzie do podkrêcania kart nvidii
Name:		nvclock
Version:	0.5
Release:	2
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.evil3d.net/pub/Evil3D/nvclock/%{name}%{version}.tar.gz
# Source0-md5:	4e07a89284702c515039f5ec22ec0a37
Source1:	nvclock.png
URL:		http://www.evil3d.net/products/nvclock/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		%{_sbindir}

%description
This program allows you to overclock your nvidia card under linux.
Warning! It can burn your graphics card!

%description -l pl
Ten program pozwala Ci na podkrêcanie Twojej karty graficznej NVidia
pod Linuksem. Uwaga! Mo¿e on spaliæ kartê graficzn±!

%package gtk
Summary:	GTK version of nvclock
Summary(pl):	nvclock z interfejsem GTK
Group:		Applications/System

%description gtk
This program allows you to overclock your nvidia card under linux.
Warning! It can burn your graphics card!

This is GTK version.

%description gtk -l pl
Ten program pozwala Ci na podkrêcanie Twojej karty graficznej NVidia
pod Linuksem. Uwaga! Mo¿e on spaliæ kartê graficzn±!

To jest wersja GTK.

%prep
%setup -q -n %{name}%{version}

%build
rm -f missing
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/System,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
cat >$RPM_BUILD_ROOT%{_applnkdir}/System/nvclock.desktop <<EOF
[Desktop Entry]
Name=nvclock
Comment=nvidia overclock utility
Comment[pl]=Narzêdzie do podkrêcania kart nvidii
Icon=nvclock.png
Exec=nvclock_gtk
Terminal=0
Type=Application
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ABOUT AUTHORS ChangeLog FAQ README
%attr(755,root,root) %{_bindir}/nvclock

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nvclock_gtk
%{_pixmapsdir}/*
%{_applnkdir}/System/*
