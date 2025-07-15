Summary:	electronics conversations
Summary(pl.UTF-8):	elektroniczne konwersacje
Name:		quendi
Version:	1.0.2
Release:	3
License:	GPL
Group:		Applications/Games
Source0:	ftp://aleph-0.dhs.org/people/loth/%{name}-%{version}.tar.gz
# Source0-md5:	5a6b5daaed703cead74a22089f1c5c55
Patch0:		%{name}-types.patch
BuildRequires:	slang-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quendi is ideology, but you can treat it like a game. That is useful
to have a conversations with androids and make electronics people. :)

%description -l pl.UTF-8
Projekt pokazujący że grafika nie jest czymś koniecznym. Ideologiczna
rozmowa z androidem przeklęte tworzenie elektronicznych postaci w
krainie ia. Nic specjalnego jeżeli traktujesz to jak grę.

%prep
%setup -q
%patch -P0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/*
%{_applnkdir}/Games/*
%{_pixmapsdir}/*
